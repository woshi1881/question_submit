from playwright.sync_api import sync_playwright
import csv
import random
#这个代码仅可抓取10个字段
def imitate_mouse_move(page):
    page.mouse.move(100,100)
def imitate_thinking(page):
    time = [1000,2000,3000,4000,5000]
    page.wait_for_timeout(random.choice(time))
def test(page,section):
    for i in range(5):
        if not page.locator(f"{section}").all_inner_texts():
            page.wait_for_timeout(2000)
        else:
            break
with (sync_playwright() as p):
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    cookies = [{
        "name": "cf_clearance",
        "domain": ".upwork.com",
        "value": "",#请自行在真实浏览器中登录而后添加对应cookies
        "path": "/"
    }]
    context.add_cookies(cookies)
    context.add_init_script('''
                  Object.defineProperty(navigator, 'webdriver', {
                    get: () => undefined
                });
                delete window.cdc_adoQpoasnfa76pfcZLmcfl_Array
                delete window.cdc_adoQpoasnfa76pfcZLmcfl_Promise
                delete window.cdc_adoQpoasnfa76pfcZLmcfl_Symbol
                       ''')
    page = context.new_page()
    page.goto("https://www.upwork.com/login",wait_until="domcontentloaded")
    imitate_mouse_move(page)
    imitate_thinking(page)
    user_name = []#请填入账号对应邮箱
    password = []#请填入账号密码
    for user,pwd in zip(user_name,password):
            page.locator("#login_username").fill(f"{user}")
            imitate_mouse_move(page)
            imitate_thinking(page)
            page.locator("#login_password_continue").click()
            imitate_mouse_move(page)
            imitate_thinking(page)
            page.locator("#login_password").fill(f"{pwd}")
            imitate_mouse_move(page)
            imitate_thinking(page)
            page.locator("#login_control_continue").click()
            imitate_mouse_move(page)
            imitate_thinking(page)
            input("请重新尝试点击登入1_3次,如果成功登录则点击enter,反之重启程序")
            page.wait_for_load_state("domcontentloaded")
    page.locator("#dropdown-trigger-freelancers_cl").click()
    page.locator('a[href="/nx/search/talent/"]').click()
    imitate_thinking(page)
    with open("freelancer_1.csv", "a", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["name", "location", "title_occupation", "salar_hour", "description", "skills", "rate_success","work_experience", "education", "language", "certification"])
        for num in range(1, 260):
            page.goto(f"https://www.upwork.com/nx/search/talent/?page={num}", wait_until="domcontentloaded")
            page.wait_for_timeout(6000)
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
                        continue
                    last_num = num
                    print(num)
                    print("start")
                    break
                except Exception as e:
                    print(f"获取失败: {e}")
                    page.wait_for_timeout(2000)
            for uid in uids:
                page.hover(f"#{uid}>.flex-1.section>.d-flex")
                page.locator(f"#{uid}>.flex-1.section>.d-flex").click()
                imitate_thinking(page)
                page.wait_for_load_state("domcontentloaded")
                test(page,'h3[itemprop="name"][class="mb-0 d-inline-flex align-items-center"]')
                name = page.locator('h3[itemprop="name"][class="mb-0 d-inline-flex align-items-center"]').all_inner_texts()
                #location = page.locator("#location-time-vertical>.d-flex.location.align-items-center.ellipsis").all_inner_texts()
                test(page,'#location-time-vertical>.d-flex.location.align-items-center.ellipsis')
                location = page.locator("#location-time-vertical>.d-flex.location.align-items-center.ellipsis").all_inner_texts()
                test(page,'.title-vertical.text-body.text-light-on-muted.mt-2x')
                title_occupation = page.locator(".title-vertical.text-body.text-light-on-muted.mt-2x").all_inner_texts()
                test(page,'.span-12.span-md-6.d-flex.justify-content-end>.air3-card.overview-card>.text-base-sm')
                salar_hour = page.locator(".span-12.span-md-6.d-flex.justify-content-end>.air3-card.overview-card>.text-base-sm").all_inner_texts()
                #salar_hour = page.locator(".span-12.span-md-6.d-flex.justify-content-end>.air3-card.overview-card>.text-base-sm").all_inner_texts()
                try:
                    page.locator('#hor-anc-id-about>.air3-truncation.break.text-pre-line.text-body.text-gray-45.mt-4x.mt-md-6x.d-block>.air3-truncation-labels>.air3-btn-link-secondary.air3-truncation-btn').click()
                except:
                    pass
                test(page,'.air3-truncation.is-expanded.break.text-pre-line.text-body.text-gray-45.mt-4x.mt-md-6x.d-block')
                description = page.locator(".air3-truncation.is-expanded.break.text-pre-line.text-body.text-gray-45.mt-4x.mt-md-6x.d-block").all_inner_texts()
                test(page,'.d-flex.list-unstyled.flex-wrap-wrap.mb-0.air3-token-wrap')
                skills = page.locator(".d-flex.list-unstyled.flex-wrap-wrap.mb-0.air3-token-wrap").all_inner_texts()
                test(page,'.span-12.span-md-6.d-flex.justify-content-end>.air3-card.overview-card>.text-base-sm')
                rate_success = page.locator(f'#{uid} span[data-test="i18n-t"]').all_inner_texts()
                revenue_all = page.locator(".span-4.d-flex.flex-column.align-items-center.air3-card.bg-muted-light.py-4x.px-1x").all_inner_texts()
                test(page,'.air3-tab-content>.air3-tab-pane.is-active')
                work_experience = page.locator(".air3-tab-content>.air3-tab-pane.is-active").all_inner_texts()
                test(page,'.d-flex.justify-space-between.mb-3x .mb-0')
                education = page.locator(".d-flex.justify-space-between.mb-3x .mb-0").all_inner_texts()+page.locator(".d-flex.justify-space-between.mb-3x .mt-3x.text-light-on-muted").all_inner_texts()
                #page.locator('#hor-anc-id-about>.air3-grid-container>.span-12.span-md-6.d-flex.justify-content-end>.air3-card.overview-card.ml-2x>span[theme="air-3-0"]').hover
                test(page,'.air3-card.overview-card.ml-2x .air3-popper-wrapper .list-unstyled .mt-2x .d-inline-block.vertical-align-middle')
                language = page.locator(".air3-card.overview-card.ml-2x .air3-popper-wrapper .list-unstyled .mt-2x .d-inline-block.vertical-align-middle").all_inner_texts()
                #language = page.locator(".text-base-sm.d-flex.flex-1.align-items-center").all_inner_texts()
                #page.locator('#hor-anc-id-about>.air3-grid-container>.span-12.span-md-6.d-flex.justify-content-end>.air3-card.overview-card.ml-2x>span[theme="air-3-0"]').click()
                #language = page.locator(".span-12.span-md-. d-flex justify-content-end .size-md.air3-popper-container").all_inner_texts()
                certification = page.locator(".air3-card-section.py-0.section-container.no-y-padding .air3-card-section.px-0 .span-9.span-md-10.certificate-details-column").all_inner_texts()
                writer.writerow([f"{name}", f"{location}", f"{title_occupation}", f"{salar_hour}", f"{description}",
                                 f"{skills}", f"{rate_success}", f"{work_experience}", f"{education}", f"{language}", f"{certification}"])
                page.locator('.d-flex.flex-1.justify-space-between.align-items-center.dynamic-profile-mobile-header>.d-flex.air3-slider-prev-btn>.air3-icon.md>svg[xmlns="http://www.w3.org/2000/svg"]').click()
                imitate_thinking(page)
            print(num)
            print("end")
            page.goto(f"https://www.upwork.com/nx/search/talent/?page={num+1}",wait_until="domcontentloaded")
            page.wait_for_timeout(6000)
        page.close()