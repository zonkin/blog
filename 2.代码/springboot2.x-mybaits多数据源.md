# springboot2.x-mybatis多数据源

1. ### application配置

 ``` application.yml配置
 #application.yml,包括部分druid配置
 spring:
   primarydatasource:  #datasource 只能用小写
     driver-class-name: com.mysql.jdbc.Driver
     url: jdbc:mysql://localhost:3306/test?useUnicode=true&amp;characterEncoding=UTF-8&amp;autoReconnect=true&amp;autoReconnectForPools=true
     username: root
     password: aaaa
     #配置初始化大小/最小/最大
     initial-size: 1
     min-idle: 1
     max-active: 20
     #获取连接等待超时时间
     max-wait: 60000
     #间隔多久进行一次检测，检测需要关闭的空闲连接
     time-between-eviction-runs-millis: 60000
     #一个连接在池中最小生存的时间
     min-evictable-idle-time-millis: 300000
     validation-query: SELECT 'x'
     test-while-idle: true
     test-on-borrow: false
     test-on-return: false
     #打开PSCache，并指定每个连接上PSCache的大小。oracle设为true，mysql设为false。分库分表较多推荐设置为false
     pool-prepared-statements: false
     max-pool-prepared-statement-per-connection-size: 20
   managedatasource:
     driver-class-name: com.mysql.jdbc.Driver
     url: jdbc:mysql://localhost:3306/test2?useUnicode=true&amp;characterEncoding=UTF-8&amp;autoReconnect=true&amp;autoReconnectForPools=true
     username: root
     password: aaaa
     #配置初始化大小/最小/最大
     initial-size: 1
     min-idle: 1
     max-active: 20
     #获取连接等待超时时间
     max-wait: 60000
     #间隔多久进行一次检测，检测需要关闭的空闲连接
     time-between-eviction-runs-millis: 60000
     #一个连接在池中最小生存的时间
     min-evictable-idle-time-millis: 300000
     validation-query: SELECT 'x'
     test-while-idle: true
     test-on-borrow: false
     test-on-return: false
     #打开PSCache，并指定每个连接上PSCache的大小。oracle设为true，mysql设为false。分库分表较多推荐设置为false
     pool-prepared-statements: false
     max-pool-prepared-statement-per-connection-size: 20

 ```

 **添加一个datasource配置，注意只能小写并且下划线会被忽略，前缀没有关系，两个datasource区分就可以**

2. ### config代码应用配置信息，分别配置datasource、SqlSessionFactory、DataSourceTransactionManager、SqlSessionTemplate

 ```主datasource
 //主datasource
 @Configuration
 @MapperScan(basePackages = "com.soft.dao.primary", sqlSessionTemplateRef = "primarySqlSessionTemplate")
 public class PrimaryDatasourceConfig {
 
     @Bean(name = "primaryDataSource")
     @ConfigurationProperties(prefix = "spring.primarydatasource")
     @Primary
     public DataSource primaryDataSource() {
         return DruidDataSourceBuilder.create().build();
     }
 
     @Bean(name = "primarySqlSessionFactory")
     @Primary
     public SqlSessionFactory primarySqlSessionFactory(@Qualifier("primaryDataSource") DataSource dataSource) throws Exception {
         SqlSessionFactoryBean bean = new SqlSessionFactoryBean();
         bean.setDataSource(dataSource);
         bean.setMapperLocations(new PathMatchingResourcePatternResolver().getResources("classpath:mapper/primary/*.xml"));
         return bean.getObject();
     }
 
     @Bean(name = "primaryTransactionManager")
     @Primary
     public DataSourceTransactionManager primaryTransactionManager(@Qualifier("primaryDataSource") DataSource dataSource) {
         return new DataSourceTransactionManager(dataSource);
     }
 
     @Bean(name = "primarySqlSessionTemplate")
     @Primary
     public SqlSessionTemplate primarySqlSessionTemplate(@Qualifier("primarySqlSessionFactory") SqlSessionFactory sqlSessionFactory) throws Exception {
         return new SqlSessionTemplate(sqlSessionFactory);
     }
 
 
 }

 ```
 ```其他datasource
 //其他datasource
 @Configuration
 @MapperScan(basePackages = "com.soft.dao.manage", sqlSessionTemplateRef = "manageSqlSessionTemplate")
 public class ManageDatasourceConfig {
 
     @Bean(name = "manageDataSource")
     @ConfigurationProperties(prefix = "spring.managedatasource")
     public DataSource manageDataSource() {
         return DruidDataSourceBuilder.create().build();
     }
 
     @Bean(name = "manageSqlSessionFactory")
     public SqlSessionFactory manageSqlSessionFactory(@Qualifier("manageDataSource") DataSource dataSource) throws Exception {
         SqlSessionFactoryBean bean = new SqlSessionFactoryBean();
         bean.setDataSource(dataSource);
         bean.setMapperLocations(new PathMatchingResourcePatternResolver().getResources("classpath:mapper/manage/*.xml"));
         return bean.getObject();
     }
 
     @Bean(name = "manageTransactionManager")
     public DataSourceTransactionManager testTransactionManager(@Qualifier("manageDataSource") DataSource dataSource) {
         return new DataSourceTransactionManager(dataSource);
     }
 
     @Bean(name = "manageSqlSessionTemplate")
     public SqlSessionTemplate primarySqlSessionTemplate(@Qualifier("manageSqlSessionFactory") SqlSessionFactory sqlSessionFactory) throws Exception {
         return new SqlSessionTemplate(sqlSessionFactory);
     }
 
 
 }
 
 ```
 **1. 必须要有一个主datasource使用``@Primary``注解标记;**

 **2. 使用``@ConfigurationProperties(prefix = "spring.xxxdatasource")``注解应用不同的配置信息;**

 **3. 配置SqlSessionFactory时要分别设置mapper的映射文件路径，建议其他内容如model文件、service文件也相应区分目录。**

3. ### 结束，其他和单数据源使用一样
