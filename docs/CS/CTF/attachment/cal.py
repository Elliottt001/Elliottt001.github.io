
import socket
import re

HOST = "10.214.160.13"
PORT = 11002

def recv_until(sock, delimiter):
    buf = b""
    delim_len = len(delimiter)
    while True:
        data = sock.recv(1)
        if not data:
            break
        buf += data
        if len(buf) >= delim_len and buf[-delim_len:] == delimiter:
            return buf[:-delim_len]
    return buf

def clean_question(raw_question):
    match = re.search(r'=\s*$', raw_question)
    if match:
        expr = raw_question[:match.start()].strip()
    else:
        expr = raw_question
    return re.sub(r'^[^\d]*(?=\d)', '', expr)

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.settimeout(15) 
        s.connect((HOST, PORT))

        for _ in range(7):
            print("[HEADER]", recv_until(s, b'\n').decode().strip())

        for q in range(20):
            question = recv_until(s, b'= ').decode().strip()
            cleaned_question = clean_question(question)
            print(f"[Q{q+1}] 清洗后表达式: {cleaned_question}")

            try:
                result = eval(cleaned_question)
                answer = str(int(result)) if isinstance(result, float) and result.is_integer() else str(result)
            except:
                raise RuntimeError(f"计算失败: {cleaned_question}")

            payload = answer.encode() + b'\r\n'  
            s.sendall(payload)
            print(f"[ANS] 发送内容: {payload!r}")

            ack = recv_until(s, b'\n').decode().strip()
            print(f"[ACK] {ack}")

        flag_data = b""
        for _ in range(3):
            flag_data += recv_until(s, b'\n') + b'\n'
        flag = re.search(r'flag\{.*?\}', flag_data.decode())
        print("\n最终结果:", flag.group(0) if flag else "未找到flag")

    except Exception as e:
        print(f"错误: {str(e)}")
    finally:
        s.close()

if __name__ == "__main__":
    main()