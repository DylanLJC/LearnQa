# driver de 复用

每次执行测试用例，都要初始化一次driver

操作： 如果driver存在，不为空，复用driver 不存在（None），就创建一个新的driver 在start（）中实现

具体实现： 1在base_page里面设置： def __init__(self, driver: WebDriver=None):  #=None设定初始值 self.driver = driver # 建立启动的实例 2 app中
start（）中进行判断

