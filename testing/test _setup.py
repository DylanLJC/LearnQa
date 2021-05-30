class TestDemo:
    def setup_class(self):
        print("类级别的setup")

    def teardown_class(self):
        print("类级别的setup")

    def setup(self):
        print("方法级别的setup")

    def teardown(self):
        print("方法级别的teardown")

    def test_demo1(self):
        print("demo1")

    def test_demo2(self):
        print("demo2")
