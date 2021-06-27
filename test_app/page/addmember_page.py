class AddMemberPage:
    def click_addmember_menual(self):
        # click[手动输入添加]
        from test_app.page.editmember_page import EditMemberPage
        return EditMemberPage()

    def get_tip(self):
        return True
