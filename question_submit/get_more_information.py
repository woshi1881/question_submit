from playwright.sync_api import sync_playwright
import csv
import random
def imitate_mouse_move(page):
    page.mouse.move(100,100)
def imitate_thinking(page):
    time = [1000,2000,3000,4000,5000]
    page.wait_for_timeout(random.choice(time))
def test(page,section):
    for i in range(1,6):
        test = page.locator(f"{section}").all_inner_texts()
        if test == []:
            page.wait_for_timeout(2000)
        else:
            break
def seek_repetition (uid):
    with open("./freelancer_2.csv", "r", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        id = []
        for row in reader:
            id.append(row["id"])
        for i in range(0, len(id)):
            if uid == id[i]:
                return "error"


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    context.add_init_script('''
                      Object.defineProperty(navigator, 'webdriver', {
                        get: () => undefined
                    });
                    delete window.cdc_adoQpoasnfa76pfcZLmcfl_Array
                    delete window.cdc_adoQpoasnfa76pfcZLmcfl_Promise
                    delete window.cdc_adoQpoasnfa76pfcZLmcfl_Symbol
                           ''')
    cookies = [{
        "name": "cf_clearance",
        "domain": ".upwork.com",
        "value": "",#请先自己登录而后将对应cookies填入
        "path": "/",
    }]
    context.add_cookies(cookies)
    page = context.new_page()
    page.goto("https://www.upwork.com/login",wait_until="domcontentloaded")
    imitate_thinking(page)
    user_name = [""]#请填入账号邮箱
    password = [""]#请填入账号密码
    page.locator("#login_username").fill(f"{user_name[0]}")
    imitate_mouse_move(page)
    imitate_thinking(page)
    page.locator("#login_password_continue").click()
    imitate_mouse_move(page)
    imitate_thinking(page)
    page.locator("#login_password").fill(f"{password[0]}")
    imitate_mouse_move(page)
    imitate_thinking(page)
    page.locator("#login_control_continue").click()
    imitate_mouse_move(page)
    imitate_thinking(page)
    error = input("请重新尝试点击登入1_3次,如果成功登录则点击enter,反之重启程序")
    page.wait_for_load_state("load")
    imitate_thinking(page)
    with open ("./freelancer_2.csv","a",encoding = "utf_8",newline = "")as f:
        writer = csv.writer(f)
        reader = csv.DictReader(f)
        writer.writerow(["id","name", "location", "title_occupation", "salar_hour", "description","skills", "rate_success", "education", "language","certification", "works","work_history","Total_earnings","book"])
        for num in range(1,261):
            page.goto(f"https://www.upwork.com/nx/search/talent?page={num}", wait_until="domcontentloaded")
            page.wait_for_timeout(10000)
            for i in range(1, 999):
                try:
                    uids = page.evaluate('''() => {
                        function search_span() {
                            for (var i = 0; i < 99; i++) {
                                var name = "span-" + i.toString();
                                var collection = document.getElementsByClassName(name);
                                for (var j = 0; j < collection.length; j++) {
                                    if (collection[j].children.length < 2)
                                        continue;
                                    if (collection[j].children[1].tagName.toLowerCase() == "section")
                                        return collection[j].children[1].children;
                                }
                            }
                            return null;
                        }

                        var uid_list = [];
                        var ele = search_span();
                        if (!ele)
                            return uid_list;
                        for (var i = 0; i < ele.length; i++) {
                            if (ele[i].tagName.toLowerCase() != "article")
                                continue;
                            var id = ele[i].getAttribute("id");
                            if (id)
                                uid_list.push(id);
                        }
                        return uid_list;
                    }''')
                    if not uids:
                        page.wait_for_timeout(2000)
                        continue
                    last_num = num
                    print(num)
                    print("start")
                    break
                except Exception as e:
                    print(f"获取失败: {e}")
                    page.wait_for_timeout(2000)
            for uid in uids:
                seek = seek_repetition(uid)
                if seek=="error":
                    continue
                page.hover(f"#{uid}>.flex-1.section>.details.mt-3x")
                page.wait_for_timeout(500)
                page.locator(f"#{uid}>.flex-1.section>.details.mt-3x").click()
                with context.expect_page() as e:
                    page.locator('.d-flex.flex-1.justify-space-between.align-items-center.dynamic-profile-mobile-header>.air3-link.air3-link-primary.air3-btn-link.align-items-center.air3-btn-link.align-items-center').click()
                    new_page = e.value
                    new_page.wait_for_load_state("domcontentloaded")
                page.wait_for_timeout(1000)
                test(new_page, '.air3-card.air3-card-sections.air3-card-outline.profile-outer-card.mb-4x>.air3-card-section>.d-flex>.flex-1.min-width-0 .identity-container .d-inline.vertical-align-middle.m-0.d-inline-flex.align-items-center.rr-mask.h2')
                name = new_page.locator('.air3-card.air3-card-sections.air3-card-outline.profile-outer-card.mb-4x>.air3-card-section>.d-flex>.flex-1.min-width-0 .identity-container .d-inline.vertical-align-middle.m-0.d-inline-flex.align-items-center.rr-mask.h2').all_inner_texts()

                test(new_page, '.air3-card.air3-card-sections.air3-card-outline.profile-outer-card.mb-4x>.air3-card-section>.d-flex>.flex-1.min-width-0 .d-flex.flex-1.justify-space-between .d-block.d-md-inline-block.location.rr-mask')
                location = new_page.locator(".air3-card.air3-card-sections.air3-card-outline.profile-outer-card.mb-4x>.air3-card-section>.d-flex>.flex-1.min-width-0 .d-flex.flex-1.justify-space-between .d-block.d-md-inline-block.location.rr-mask").all_inner_texts()

                test(new_page, '.air3-grid-container.gap-0.position-relative .air3-card-section>.mb-10x>.d-flex.align-items-center.justify-space-between>div:nth-child(1)')
                title_occupation = new_page.locator(".air3-grid-container.gap-0.position-relative .air3-card-section>.mb-10x>.d-flex.align-items-center.justify-space-between>div:nth-child(1)").all_inner_texts()

                test(new_page, '.air3-grid-container.gap-0.position-relative .air3-card-section>.mb-10x>.d-flex.align-items-center.justify-space-between>div:nth-child(2)')
                salar_hour = new_page.locator(".air3-grid-container.gap-0.position-relative .air3-card-section>.mb-10x>.d-flex.align-items-center.justify-space-between>div:nth-child(2)").all_inner_texts()

                try:
                    new_page.locator('.air3-grid-container.gap-0.position-relative .air3-card-section>.d-flex.justify-space-between>.air3-line-clamp-wrapper>button').click()
                except:
                    pass
                test(new_page,'.air3-grid-container.gap-0.position-relative .air3-card-section>.d-flex.justify-space-between>.air3-line-clamp-wrapper>div')
                description = new_page.locator(".air3-grid-container.gap-0.position-relative .air3-card-section>.d-flex.justify-space-between>.air3-line-clamp-wrapper>div").all_inner_texts()

                test(new_page, '.air3-card.air3-card-sections.air3-card-outline.profile-outer-card.mb-4x>.air3-card-section>.skills>.d-flex.list-unstyled.flex-wrap-wrap.mb-0.air3-token-wrap')
                skills = new_page.locator(".air3-card.air3-card-sections.air3-card-outline.profile-outer-card.mb-4x .air3-card-section>.skills>ul").all_inner_texts()

                test(new_page, '.air3-card.air3-card-sections.air3-card-outline.profile-outer-card>.air3-card-section>.mt-1 .d-inline-block.air3-popper-trigger .air3-progress-circle')
                rate_success = new_page.locator('.air3-card.air3-card-sections.air3-card-outline.profile-outer-card.mb-4x>.air3-card-section>.d-flex .d-flex.flex-1.flex-column.min-width-0>.d-flex .air3-progress-circle>span>span:nth-child(1)').all_inner_texts()

                Total_earnings = new_page.locator(".air3-grid-container.gap-0.position-relative .air3-card-sections.pt-0>.air3-card-section .d-flex.space-between>div:nth-child(1)>div:nth-child(1)").all_inner_texts()


                test(new_page, '.air3-card.air3-card-sections.air3-card-outline.profile-outer-card.my-4x>.air3-card-section>.air3-card-sections .air3-card-section.px-0')
                work_history = new_page.locator(".air3-card.air3-card-sections.air3-card-outline.profile-outer-card.my-4x>.air3-card-section>.air3-card-sections .air3-card-section.px-0").all_inner_texts()

                test(new_page, '.air3-card.air3-card-outline.profile-outer-card.my-4x>.air3-card-sections>.list-unstyled>.air3-card-section.px-0.mb-0')
                education = new_page.locator(".air3-card.air3-card-outline.profile-outer-card.my-4x>.air3-card-sections>.list-unstyled>.air3-card-section.px-0.mb-0").all_inner_texts()
                test(page,'.air3-grid-container.gap-0.position-relative .air3-card-sections.pt-0>.air3-card-section.air3-grid-container.template-col-1>div:nth-child(3)>.list-unstyled')
                language = new_page.locator(".air3-grid-container.gap-0.position-relative .air3-card-sections.pt-0>.air3-card-section.air3-grid-container.template-col-1 .list-unstyled").all_inner_texts()

                test(new_page,".air3-card-section>.vue-portal-target>.portfolio-v2-viewer-shelf.d-flex.flex-column>.position-relative>.air3-grid-container.mt-4x")
                book = new_page.locator(".air3-card-section>.vue-portal-target>.portfolio-v2-viewer-shelf.d-flex.flex-column>.position-relative>.air3-grid-container.mt-4x").all_inner_texts()
                test(new_page,".air3-card-section.work-history-section>.work-history>div:nth-child(2)>.air3-tabs.up-cfe-work-history-tabs>.air3-tab-content")
                works = new_page.locator(".air3-card-section.work-history-section>.work-history>div:nth-child(2)>.air3-tabs.up-cfe-work-history-tabs>.air3-tab-content").all_inner_texts()
                certification = new_page.locator(".air3-card.air3-card-sections.air3-card-outline.profile-outer-card.my-4x>.air3-card-sections .air3-card-section.mx-6x.mx-md-0.px-0.px-md-8x>div>div:nth-child(2)>div:nth-child(1)").all_inner_texts()

                writer.writerow([f"{uid}",f"{name}", f"{location}", f"{title_occupation}", f"{salar_hour}", f"{description}",
                                         f"{skills}", f"{rate_success}", f"{education}", f"{language}",
                                         f"{certification}", f"{works}",f"{work_history}",f"{Total_earnings}",f"{book}"])
                print("end")
                new_page.close()
                page.locator('.d-flex.flex-1.justify-space-between.align-items-center.dynamic-profile-mobile-header>.d-flex.air3-slider-prev-btn>.air3-icon.md>svg[xmlns="http://www.w3.org/2000/svg"]').click()
        page.close()