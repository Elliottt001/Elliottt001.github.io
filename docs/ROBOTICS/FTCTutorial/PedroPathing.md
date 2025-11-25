## Pedro Pathing 路径跟随算法

参考文献：
- https://www.bilibili.com/video/BV1YQCvYTEmT/?spm_id_from=333.337.search-card.all.click&vd_source=b14909f255fe42946743657320d2f59a
- https://zhuanlan.zhihu.com/p/344934774
- https://math.hws.edu/eck/cs424/notes2013/canvas/bezier.html


### 算法 Algorithm

Pedro Pathing 的核心在于生成和执行一个“驱动向量”来指导机器人的运动，这个过程通常涉及以下几个关键部分：

1.  **路径生成 (Path Generation)：**
    * 使用贝塞尔曲线来定义路径。用户可以指定控制点 (Control Points) 来塑造曲线的形状。
2.  **定位与误差计算 (Localization and Error)：**
    * 机器人通过定位系统（如使用全向轮或万向轮驱动的里程计/定位轮）获取当前的 **位姿 (Pose)**，即 $(x, y)$ 坐标和朝向角 $(\theta)$。
    * 算法计算机器人当前位置距离路径上的**最近点 (Closest Point)** 的距离（误差）和方向。
3.  **驱动向量计算 (Drive Vector Algorithm)：**
    * 这是算法的核心，它计算一个**目标速度和方向的向量**。
    * **目标速度计算：** 根据剩余距离 $s$ 和设定的最大减速度 $a_t$（通常是负值），利用运动学公式计算出在路径终点刚好能停下的**目标速度** $v_t$：
        $$\text{目标速度} \ v_t = \sqrt{-2 \cdot a_t \cdot s}$$
    * **误差控制 (PIDF)：** 使用 PIDF 控制器，结合目标速度和实时误差，计算出实际驱动所需的功率或速度指令。
4.  **运动指令执行 (Execution)：**
    * 将计算出的向量转换为各个车轮的实际功率或速度指令，驱动机器人沿着贝塞尔曲线平滑且快速地前进。

## 实现 Imeplementation

### 1\. 几何与定位类 (Geometry & Localization)

用于表示机器人在场上的位置和朝向。

| 类/方法 | 描述 | 示例用法 |
| :--- | :--- | :--- |
| `Pose` 类 | 表示机器人在场上的 **位姿** (位置和朝向)：**$(x, y, \theta)$**。它是路径的输入和跟随器的输出。 | `new Pose(20, 30, Math.toRadians(90))` |
| `BezierLine` 类 | 表示一条**贝塞尔曲线**。通常由两个 `Pose` (起点和终点) 定义，也可以加入控制点。 | `new BezierLine(startPose, endPose)` |
| `Follower` 类 | 路径跟随器的**主控制类**。它包含机器人的定位系统和驱动方法。 | `follower = Constants.createFollower(hardwareMap);` |
| `follower.getPose()` | 实时获取跟随器内部维护的机器人当前 `Pose`。用于路径构建和显示。 | `Pose current = follower.getPose();` |
| `follower.setStartingPose()` | 设置自动驾驶开始时机器人的初始位置。 | `follower.setStartingPose(startPose);` |

-----

### 2\. 路径构建 (Path Building)

使用 `PathBuilder` 来链式地定义由贝塞尔曲线组成的复杂路径。

| 类/方法 | 描述 | 示例用法 |
| :--- | :--- | :--- |
| `PathChain` 类 | 路径链，包含了需要按顺序执行的一系列 `Path`（路径）。 | (通常由 `PathBuilder.build()` 返回) |
| `PathBuilder` 类 | 用于链式构造 `PathChain` 的构建器。 | `follower.pathBuilder()...` |
| `.addPath(Path)` | 向路径链中添加一条路径（通常是 `BezierLine` 或 `Path`）。 | `.addPath(new Path(line))` |
| `.setHeadingInterpolation(...)` | **设置航向插值器。** 决定机器人在跟随路径时如何改变朝向（$\theta$）。 | `.setHeadingInterpolation(HeadingInterpolator.linearFromPoint(currentHeading, targetHeading, 0.8))` |
| `.build()` | 完成路径构建，返回一个可执行的 `PathChain` 对象。 | `PathChain path = pathBuilder.build();` |

-----

### 3\. 路径执行与控制 (Path Execution & Control)

用于启动和管理路径跟随过程。

| 类/方法 | 描述 | 示例用法 |
| :--- | :--- | :--- |
| `follower.followPath(PathChain)` | **启动**机器人对给定 `PathChain` 的跟随。这是一个**非阻塞**方法（即函数立即返回）。 | `follower.followPath(path);` |
| `follower.update()` | **在循环中调用！** 实时更新跟随器的状态，计算驱动向量，并设置电机功率。这是反应式跟随的核心。 | `while (opModeIsActive()) { follower.update(); }` |
| `follower.isBusy()` | 检查跟随器是否仍在跟随路径（即路径尚未完成）。常用于自动驾驶中的等待。 | `while (opModeIsActive() && follower.isBusy()) { follower.update(); }` |
| `follower.setMotorPowers(double x, double y, double h)` | **底层驱动方法。** 设置机器人在场坐标系下的 X 轴速度、Y 轴速度和旋转角速度（Heading）。（通常在 `follower.update()` 内部调用，用户一般无需直接调用） | （内部调用） |

-----

### 4\. 路径回调 (Path Callbacks)

用于在路径执行过程中触发特定动作（例如放下机械臂或吸取物品）。

| 类/方法 | 描述 | 示例用法 |
| :--- | :--- | :--- |
| `PathCallback` 接口 | 定义一个在路径上特定点执行的动作。 | （用户自定义动作的接口） |
| `.addParametricCallback(double percent, Runnable action)` | 添加**参数回调**。当路径完成度达到某一百分比时执行 `action`。这是最推荐的回调类型。 | `pathBuilder.addParametricCallback(0.5, () -> { // 执行机械臂操作 });` |
| `.addPoseCallback(Pose pose, Runnable action, double guess)` | **位姿回调。** 当机器人到达路径上**最接近**给定 `Pose` 的点时执行 `action`。 | `pathBuilder.addPoseCallback(checkPoint, () -> { // 执行传感器读取 }, 0.5);` |

-----

### 流程示例 (Java OpMode)

在 FTC 的 `LinearOpMode` 中，Pedro Pathing 的基本使用流程如下：

```java
import com.pedropathing.follower.Follower;
import com.pedropathing.geometry.BezierLine;
import com.pedropathing.geometry.Pose;
import com.pedropathing.paths.HeadingInterpolator;
import com.pedropathing.paths.Path;
import com.pedropathing.paths.PathChain;

public class MyPedroAuto extends LinearOpMode {
    @Override
    public void runOpMode() {
        // 1. 初始化 Follower 和定位系统
        Follower follower = Constants.createFollower(hardwareMap);
        
        Pose startPose = new Pose(0, 0, 0);
        Pose waypoint = new Pose(50, 50, Math.toRadians(90));
        Pose endPose = new Pose(100, 0, Math.toRadians(180));

        follower.setStartingPose(startPose);
        follower.update(); // 第一次更新以初始化内部状态

        // 2. 构建路径链 PathChain
        PathChain path = follower.pathBuilder()
                // 第一段路径：直线到 Waypoint，线性插值朝向
                .addPath(new Path(new BezierLine(startPose, waypoint)))
                .setHeadingInterpolation(HeadingInterpolator.linearFromPoint(startPose.getHeading(), waypoint.getHeading(), 0.8))
                .addParametricCallback(0.8, () -> {
                    telemetry.addData("Status", "Passing Waypoint 80%");
                })

                // 第二段路径：从 Waypoint 弯曲到 EndPose，固定朝向
                .addPath(new Path(new BezierLine(waypoint, endPose)))
                .setHeadingInterpolation(HeadingInterpolator.constantHeading(waypoint.getHeading()))

                .build();

        // 3. 等待 OpMode 启动
        waitForStart();

        // 4. 执行路径
        if (opModeIsActive()) {
            follower.followPath(path);

            // 5. 实时循环更新跟随器状态，直到路径完成
            while (opModeIsActive() && follower.isBusy()) {
                follower.update();
                telemetry.addData("Current Pose", follower.getPose().toString());
                telemetry.update();
            }
        }
    }
}
```

您希望进一步了解如何**调优 PIDF 控制器**或**自定义定位系统**（Localizer）的细节吗？
