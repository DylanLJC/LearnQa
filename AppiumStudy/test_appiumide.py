from appium import webdriver

desire_cpa = {
    "platformName": "android",
    "appPackage": "com.xueqiu.android",
    "appActivity": ".view.WelcomeActivityAlias"
}
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_cpa)
driver.implicitly_wait(5)
el1 = driver.find_element_by_id("com.xueqiu.android:id/tv_search")
el1.click()
el3 = driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
el3.send_keys("阿里巴巴")
el4 = driver.find_element_by_xpath(
    "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.LinearLayout/android.widget.TextView[1]")
el4.click()
