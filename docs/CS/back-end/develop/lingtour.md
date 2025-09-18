项目结构

```
LingTour/
├── .git/
├── .gitattributes
├── .gitignore
├── .mvn/
├── .vscode/
├── HELP.md
├── mvnw
├── mvnw.cmd
├── pom.xml
├── src/
│   ├── main/
│   │   ├── java/
│   │   │   └── com/
│   │   │       └── lingtour/
│   │   │           ├── LingTourApplication.java
│   │   │           ├── config/
│   │   │           │   ├── SecurityConfig.java
│   │   │           │   ├── WebConfig.java
│   │   │           │   └── DatabaseConfig.java
│   │   │           ├── controller/
│   │   │           │   ├── UserController.java
│   │   │           │   ├── ProductController.java
│   │   │           │   ├── TripController.java
│   │   │           │   ├── OrderController.java
│   │   │           │   ├── FavoriteController.java
│   │   │           │   └── ReviewController.java
│   │   │           ├── dto/
│   │   │           │   ├── UserDTO.java
│   │   │           │   ├── ProductDTO.java
│   │   │           │   ├── TripDTO.java
│   │   │           │   └── OrderDTO.java
│   │   │           ├── exception/
│   │   │           │   ├── GlobalExceptionHandler.java
│   │   │           │   └── CustomException.java
│   │   │           ├── model/
│   │   │           │   ├── User.java
│   │   │           │   ├── Product.java
│   │   │           │   ├── Trip.java
│   │   │           │   ├── Order.java
│   │   │           │   ├── Favorite.java
│   │   │           │   └── Review.java
│   │   │           ├── repository/
│   │   │           │   ├── UserRepository.java
│   │   │           │   ├── ProductRepository.java
│   │   │           │   ├── TripRepository.java
│   │   │           │   ├── OrderRepository.java
│   │   │           │   ├── FavoriteRepository.java
│   │   │           │   └── ReviewRepository.java
│   │   │           ├── service/
│   │   │           │   ├── UserService.java
│   │   │           │   ├── ProductService.java
│   │   │           │   ├── TripService.java
│   │   │           │   ├── OrderService.java
│   │   │           │   ├── FavoriteService.java
│   │   │           │   └── ReviewService.java
│   │   │           └── utils/
│   │   │               ├── JwtUtils.java
│   │   │               ├── DateUtils.java
│   │   │               └── FileUtils.java
│   │   ├── resources/
│   │   │   ├── application.properties
│   │   │   ├── static/
│   │   │   └── templates/
│   └── test/
│       ├── java/
│       │   └── com/
│       │       └── lingtour/
│       │           ├── LingTourApplicationTests.java
│       │           ├── repository/
│       │           │   ├── UserRepositoryTest.java
│       │           │   ├── ProductRepositoryTest.java
│       │           │   └── TripRepositoryTest.java
│       │           ├── service/
│       │           │   ├── UserServiceTest.java
│       │           │   ├── ProductServiceTest.java
│       │           │   └── TripServiceTest.java
│       │           └── controller/
│       │               ├── UserControllerTest.java
│       │               ├── ProductControllerTest.java
│       │               └── TripControllerTest.java
└── target/
```