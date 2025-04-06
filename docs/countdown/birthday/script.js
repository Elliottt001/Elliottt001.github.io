/**
 * 农历数据：1900～2050年的数据，每个元素的低 16 位代表当年各个月份的大小（0表示29天，1表示30天），
 * 低 4 位表示闰月月份（0 表示无闰月）。最高 4 位表示闰月的大小（0:29天, 1:30天）。
 * 数据来源于万年历算法，适用于常见转换。
 */
var lunarInfo = [
  0x04bd8, 0x04ae0, 0x0a570, 0x054d5, 0x0d260, 0x0d950, 0x16554, 0x056a0,
  0x09ad0, 0x055d2, 0x04ae0, 0x0a5b6, 0x0a4d0, 0x0d250, 0x1d255, 0x0b540,
  0x0d6a0, 0x0ada2, 0x095b0, 0x14977, 0x04970, 0x0a4b0, 0x0b4b5, 0x06a50,
  0x06d40, 0x1ab54, 0x02b60, 0x09570, 0x052f2, 0x04970, 0x06566, 0x0d4a0,
  0x0ea50, 0x06e95, 0x05ad0, 0x02b60, 0x186e3, 0x092e0, 0x1c8d7, 0x0c950,
  0x0d4a0, 0x1d8a6, 0x0b550, 0x056a0, 0x1a5b4, 0x025d0, 0x092d0, 0x0d2b2,
  0x0a950, 0x0b557, 0x06ca0, 0x0b550, 0x15355, 0x04da0, 0x0a5d0, 0x14573,
  0x052d0, 0x0a9a8, 0x0e950, 0x06aa0, 0x0aea6, 0x0ab50, 0x04b60, 0x0aae4,
  0x0a570, 0x05260, 0x0f263, 0x0d950, 0x05b57, 0x056a0, 0x096d0, 0x04dd5,
  0x04ad0, 0x0a4d0, 0x0d4d4, 0x0d250, 0x0d558, 0x0b540, 0x0b5a0, 0x195a6,
  0x095b0, 0x049b0, 0x0a974, 0x0a4b0, 0x0b27a, 0x06a50, 0x06d40, 0x0af46,
  0x0ab60, 0x09570, 0x04af5, 0x04970, 0x064b0, 0x074a3, 0x0ea50, 0x06b58,
  0x05ac0, 0x0ab60, 0x096d5, 0x092e0, 0x0c960, 0x0d954, 0x0d4a0, 0x0da50,
  0x07552, 0x056a0, 0x0abb7, 0x025d0, 0x092d0, 0x0cab5, 0x0a950, 0x0b4a0,
  0x0baa4, 0x0ad50, 0x055d9, 0x04ba0, 0x0a5b0, 0x15176, 0x052b0, 0x0a930,
  0x07954, 0x06aa0, 0x0ad50, 0x05b52, 0x04b60, 0x0a6e6, 0x0a4e0, 0x0d260,
  0x0ea65, 0x0d530, 0x05aa0, 0x076a3, 0x096d0, 0x04bd7, 0x04ad0, 0x0a4d0,
  0x1d0b6, 0x0d250, 0x0d520, 0x0dd45, 0x0b5a0, 0x056d0, 0x055b2, 0x049b0,
  0x0a577, 0x0a4b0, 0x0aa50, 0x1b255, 0x06d20, 0x0ada0
];

/**
 * 计算农历年份的总天数
 */
function lunarYearDays(year) {
  var i, sum = 348;
  var info = lunarInfo[year - 1900];
  // 0x8000从高位开始，依次判断12个月是否为大月（30天）
  for (i = 0x8000; i > 0x8; i >>= 1) {
    sum += (info & i) ? 1 : 0;
  }
  return sum + lunarLeapDays(year);
}

/**
 * 计算农历闰月的天数
 */
function lunarLeapDays(year) {
  if (leapMonth(year)) {
    return (lunarInfo[year - 1900] & 0x10000) ? 30 : 29;
  }
  return 0;
}

/**
 * 计算农历某月的天数
 */
function lunarMonthDays(year, month) {
  return (lunarInfo[year - 1900] & (0x10000 >> month)) ? 30 : 29;
}

/**
 * 取得农历闰月，若没有闰月则返回0
 */
function leapMonth(year) {
  return lunarInfo[year - 1900] & 0xf;
}

/**
 * 将农历日期转换为公历日期
 * 参数：
 *    lunarYear  - 农历年份
 *    lunarMonth - 农历月份（1-12）
 *    lunarDay   - 农历日（1-30）
 *    isLeapMonth - 是否为闰月（布尔值）
 * 返回值：Date对象（公历日期）
 */
function convertLunarToSolar(lunarYear, lunarMonth, lunarDay, isLeapMonth) {
  // 1900年1月31日为农历1900年正月初一
  var baseDate = new Date(1900, 0, 31);
  var offset = 0;
  var i, temp;
  
  // 累加1900年到目标年前一年的天数
  for (i = 1900; i < lunarYear; i++) {
    offset += lunarYearDays(i);
  }
  
  // 计算当年各个月的天数
  var leap = leapMonth(lunarYear);
  for (i = 1; i < lunarMonth; i++) {
    offset += lunarMonthDays(lunarYear, i);
    // 若该月为闰月，则加上闰月天数
    if (i === leap) {
      offset += lunarLeapDays(lunarYear);
    }
  }
  
  // 如果目标月份正好是闰月，则判断是否已经过了闰月
  if (isLeapMonth && (lunarMonth === leap)) {
    offset += lunarMonthDays(lunarYear, lunarMonth);
  }
  
  // 加上当前月份的天数（-1是因为农历初一对应偏移0）
  offset += lunarDay - 1;
  
  // 得到对应的公历日期
  var solarDate = new Date(baseDate.getTime() + offset * 86400000);
  return solarDate;
}

/**
 * 更新倒计时（农历生日：农历三月初十，不考虑闰月情况）
 */
function updateCountdown() {
  const now = new Date();
  let year = now.getFullYear();
  
  // 获取今年农历三月初十对应的公历日期（非闰月）
  let birthDate = convertLunarToSolar(year, 3, 10, false);
  
  // 如果今天已过今年生日，则计算明年的
  if (now > birthDate) {
    birthDate = convertLunarToSolar(year + 1, 3, 10, false);
  }
  
  const distance = birthDate - now;
  const days = Math.floor(distance / (1000 * 60 * 60 * 24));
  const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
  const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
  const seconds = Math.floor((distance % (1000 * 60)) / 1000);
  
  // 简单动画效果更新数字
  function animateNumber(element, value) {
    const str = value.toString().padStart(2, '0');
    if (element.textContent !== str) {
      element.style.transform = 'rotateX(90deg)';
      setTimeout(() => {
        element.textContent = str;
        element.style.transform = 'rotateX(0deg)';
      }, 150);
    }
  }
  
  animateNumber(document.getElementById('days'), days);
  animateNumber(document.getElementById('hours'), hours);
  animateNumber(document.getElementById('minutes'), minutes);
  animateNumber(document.getElementById('seconds'), seconds);
}

updateCountdown();
setInterval(updateCountdown, 1000);
