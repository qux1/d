import requests,random,time,uuid,string,json,re,os
from colorama import Fore,init



class Report:
    def __init__(self) -> None:

        
        self.cookies = []

        self.accounts = []

        self.stories = []

        self.done =  0
        self.error = 0
        self.sleep = 15

        init(autoreset=True)

        self.logo = """


     
      
░██╗░░░░░░░██╗░█████╗░██╗░░░░░███████╗  ████████╗███████╗░█████╗░███╗░░░███╗
░██║░░██╗░░██║██╔══██╗██║░░░░░██╔════╝  ╚══██╔══╝██╔════╝██╔══██╗████╗░████║
░╚██╗████╗██╔╝██║░░██║██║░░░░░█████╗░░  ░░░██║░░░█████╗░░███████║██╔████╔██║
░░████╔═████║░██║░░██║██║░░░░░██╔══╝░░  ░░░██║░░░██╔══╝░░██╔══██║██║╚██╔╝██║
░░╚██╔╝░╚██╔╝░╚█████╔╝███████╗██║░░░░░  ░░░██║░░░███████╗██║░░██║██║░╚═╝░██║
░░░╚═╝░░░╚═╝░░░╚════╝░╚══════╝╚═╝░░░░░  ░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝

       this is a praivate tool 

      coded by @mdip
        
        """

        print(Fore.RED + self.logo)
        
        
        self.uid = str(uuid.uuid4())

        self.load_accounts()


    def load_accounts(self):

        load = int(input(Fore.LIGHTCYAN_EX +  "[ 1 ] Login\n[ 2 ] Use cookies\n=>"))

        if load == 1:


            for account in open('accounts.txt','r').read().splitlines():
                
                user = account.split(":")[0]
                password = account.split(":")[1]

                self.login(user,password)
            if len(self.cookies) > 0:
                self.get_info()
            else:
                input(Fore.RED +  "[ \ ] enter to exit ...")
                exit()
        else:

            for account in open('cookies.txt','r').read().splitlines():
                
               self.cookies.append(account)
            if len(self.cookies) > 0:
                self.get_info()
            else:
                input(Fore.RED +"[ \ ] enter to exit ...")
                exit()

    
    def login(self,user,password):
        f=open('cookies.txt','w')
        f.close()
        headers = {
          'User-Agent':
              'Instagram 152.0.0.1.60 Android (28/9; 480dpi; 1080x2137; HUAWEI; JKM-LX1; HWJKM-H; kirin710; en_US; 216817344)',
          'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
          "Accept-Language": "Accept-Language",
          'Host': 'i.instagram.com',
          "X-IG-Connection-Type": "WIFI",
          "X-IG-Capabilities": "3brTvw==",
          'accept-encoding': 'gzip, deflate',
          "Accept": "*/*"
        }

        data = {
          "jazoest": "22452",
          "phone_id": self.uid,
          "enc_password": f"#PWD_INSTAGRAM:0:0:{password}",
          "username": user,
          "adid": self.uid,
          "guid": self.uid,
          "device_id": self.uid,
          "google_tokens": "[]",
          "login_attempt_count": "0"
        }

        req = requests.post("https://i.instagram.com/api/v1/accounts/login/",headers=headers,data=data)
        if req.text.__contains__("logged_in_user"):
            cookies = req.cookies['sessionid']
            self.cookies.append(cookies)
            print(Fore.LIGHTGREEN_EX +  f"[ + ] Logged in with {user}")
            with open('cookies.txt','a') as w :
                w.write(f'{cookies}\n')
        elif req.text.__contains__('checkpoint_required'):
            print(Fore.LIGHTBLUE_EX +  f"[ ! ] checkpoint_required {user}")
        else:
            print(Fore.RED +  f"[ X ] User or password is incorrect.")

    def get_info(self):
        self.target = str(input(Fore.LIGHTCYAN_EX +  "[ + ] Enter Target : "))
        self.get_target()
        self.report_place = int(input(Fore.LIGHTCYAN_EX +"[ 1 ] Report Profile\n[ 2 ] Report Stories\n=>"))
        self.report_type = int(input(Fore.LIGHTCYAN_EX +"[ 1 ] Spam\n[ 2 ] Self\n[ 3 ] Hate\n[ 4 ] Violence\n[ 5 ] Nudity\n[ 6 ] Bullying\n[ 7 ] Drugs\n=>"))
        self.sleep = int(input(Fore.YELLOW +"[ + ] Sleep : "))

        if self.report_place == 1:
            self.report_profile()
        else:
            self.get_stories()
            self.report_stories()

    def get_target(self):
        headers = {
            'X-IG-App-Locale': 'en_US',
            'X-IG-Device-Locale': 'en_US',
            'X-IG-Mapped-Locale': 'en_US',
            'X-IG-Connection-Type': 'WIFI',
            'X-IG-Capabilities': '3brTvw8=',
            'User-Agent':
                'Instagram 148.0.0.33.121 Android (28/9; 480dpi; 1080x2137; HUAWEI; JKM-LX1; HWJKM-H; kirin710; en_US; 216817344)',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Host': 'i.instagram.com',
            'Cookie': f'sessionid={self.cookies[0]}'

        }
        req = requests.get(f"https://www.instagram.com/api/v1/users/web_profile_info/?username={self.target}",headers=headers)

        try:
            self.user_id = str(req.json()['data']['user']['id'])
        except:
            print("[ X ] No target found enter to exit ...")
            input()
            exit()

    def report_profile(self):
        while True:
            for cookie in self.cookies:

                try:

                    headers = {
                    'Host': 'i.instagram.com',
                    'X-Ig-App-Locale': 'en_US',
                    'X-Ig-Device-Locale': 'en_US',
                    'X-Ig-Mapped-Locale': 'en_US',
                    'X-Pigeon-Session-Id': 'UFS-0e5afa95-b45f-4aa8-af41-9e039533d67b-0',
                    'X-Pigeon-Rawclienttime': '1678118511.889',
                    'X-Ig-Bandwidth-Speed-Kbps': '3828.000',
                    'X-Ig-Bandwidth-Totalbytes-B': '3185285',
                    'X-Ig-Bandwidth-Totaltime-Ms': '572',
                    'X-Ig-App-Startup-Country': 'IQ',
                    'X-Bloks-Version-Id':
                        '0ee04a4a6556c5bb584487d649442209a3ae880ae5c6380b16235b870fcc4052',
                    'X-Ig-Www-Claim': 'hmac.AR1aWEsDw6WfWexHDkfbg_-temKojpBG0NZXzjGWwnoWouO9',
                    'X-Bloks-Is-Layout-Rtl': 'false',
                    'X-Ig-Device-Id': '59579ca5-e663-4fee-b090-e8fcc8f193f3',
                    'X-Ig-Family-Device-Id': 'e921fc15-0499-46dc-943d-3350f6b3fa02',
                    'X-Ig-Android-Id': 'android-f2e05b426b619b1b',
                    'X-Ig-Timezone-Offset': '10800',
                    'User-Agent':
                        'Instagram 265.0.0.19.301 Android (30/11; 420dpi; 1080x1794; Google/google; sdk_gphone_x86; generic_x86_arm; ranchu; en_US; 436384447)',
                    'Accept-Language': 'en-US',
                    'X-Mid': 'ZAYOQQABAAGyslKmLdaVOc4U-ScJ',
                    'Cookie':f'sessionid={cookie}',
                    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                    }
                    data = {
                    'logging_extra':
                        '{"shopping_session_id":"cfbbb3a7-3ac5-46af-9758-ed56e276a6a8","nua_action":"","profile_media_attribution":"3051953907119822885_'+self.user_id+'","navigation_chain":"MainFeedFragment:feed_timeline:1:cold_start:1678118499.611:10#230#301:3051953907119822885,UserDetailFragment:profile:2:media_owner:1678118504.773::,ProfileMediaTabFragment:profile:3:button:1678118505.813::"}',
                    'trigger_event_type': 'ig_report_button_clicked',
                    'trigger_session_id': '9839a54a-e2f0-435a-8ea6-fd824f3436b4',
                    'ig_container_module': 'profile',
                    'entry_point': 'chevron_button',
                    'preloading_enabled': '1',
                    '_uuid': '59579ca5-e663-4fee-b090-e8fcc8f193f3',
                    'ig_object_value': self.user_id,
                    'ig_object_type': '5',
                    'bk_client_context':
                        '{"bloks_version":"0ee04a4a6556c5bb584487d649442209a3ae880ae5c6380b16235b870fcc4052","styles_id":"instagram"}',
                    'ixt_initial_screen_id': '030d7198-c869-4c88-ae1e-d5cf46b84aa5',
                    'bloks_versioning_id':
                        '0ee04a4a6556c5bb584487d649442209a3ae880ae5c6380b16235b870fcc4052',
                    'location': 'ig_profile',
                    }

                    req = requests.post('https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.ig.ixt.triggers.bottom_sheet.ig_content/',headers=headers,data=data)
                    
                    context = re.search(r', \"tag_selection_screen\", \"(.*?)\", ',str(req.json())).group(1)
                    data = {
                    'params':
                        '{"client_input_params":{"tags":["ig_its_inappropriate"]},"server_params":{"show_tag_search":0,"serialized_state":"'+context+'","INTERNAL__latency_qpl_marker_id":36707139,"INTERNAL__latency_qpl_instance_id":55984413600117,"is_bloks":1,"tag_source":"tag_selection_screen"}}',
                    '_uuid': 'b1080837-c663-4cbe-9951-7b18c766e54a',
                    'bk_client_context':
                        '{"bloks_version":"0ee04a4a6556c5bb584487d649442209a3ae880ae5c6380b16235b870fcc4052","styles_id":"instagram"}',
                    'bloks_versioning_id':
                        '0ee04a4a6556c5bb584487d649442209a3ae880ae5c6380b16235b870fcc4052',
                    }
                    req = requests.post('https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.instagram_bloks_bottom_sheet.ixt.screen.frx_tag_selection_screen/',data=data,headers=headers)
                    context = re.search(r', \"tag_selection_screen\", \"(.*?)\", ',str(req.json())).group(1)

                    # [ 1 ] Spam\n[ 2 ] Self\n[ 3 ] Hate\n[ 4 ] Violence\n[ 5 ] Nudity\n[ 6 ] Bullying\n[ 7 ] Drugs\n=>
                    if self.report_type == 1:
                        data = {
                            'params':
                                '{"client_input_params":{"tags":["ig_spam_v3","ig_report_account","ig_its_inappropriate"]},"server_params":{"show_tag_search":0,"serialized_state":"'+context+'","INTERNAL__latency_qpl_marker_id":36707139,"INTERNAL__latency_qpl_instance_id":74958009200047,"is_bloks":1,"tag_source":"tag_selection_screen"}}',
                            '_uuid': 'b1080837-c663-4cbe-9951-7b18c766e54a',
                            'bk_client_context':
                                '{"bloks_version":"0ee04a4a6556c5bb584487d649442209a3ae880ae5c6380b16235b870fcc4052","styles_id":"instagram"}',
                            'bloks_versioning_id':
                                '0ee04a4a6556c5bb584487d649442209a3ae880ae5c6380b16235b870fcc4052',
                        }
                        req = requests.post('https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.instagram_bloks_bottom_sheet.ixt.screen.frx_tag_selection_screen/',data=data,headers=headers)
                        if req.text.__contains__('"status":"ok"'):
                            self.done += 1
                        else:
                            self.error += 1
                    elif self.report_type == 2:
                        data = {
                            'params':
                                '{"client_input_params":{"tags":["ig_self_injury_v3","ig_its_inappropriate"]},"server_params":{"show_tag_search":0,"serialized_state":"'+context+'","INTERNAL__latency_qpl_marker_id":36707139,"INTERNAL__latency_qpl_instance_id":56827620300117,"is_bloks":1,"tag_source":"tag_selection_screen"}}',
                            '_uuid': 'b1080837-c663-4cbe-9951-7b18c766e54a',
                            'bk_client_context':
                                '{"bloks_version":"0ee04a4a6556c5bb584487d649442209a3ae880ae5c6380b16235b870fcc4052","styles_id":"instagram"}',
                            'bloks_versioning_id':
                                '0ee04a4a6556c5bb584487d649442209a3ae880ae5c6380b16235b870fcc4052',
                        }

                        req = requests.post('https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.instagram_bloks_bottom_sheet.ixt.screen.frx_tag_selection_screen/',data=data,headers=headers)
                        context = re.search(r'\"report\", \"(.*?)\", ',str(req.json())).group(1)
                        data = {
                            'params':
                                '{"server_params":{"serialized_state":"'+context+'","INTERNAL__latency_qpl_marker_id":36707139,"INTERNAL__latency_qpl_instance_id":57131417800002,"selected_option":"report"}}',
                            '_uuid': 'b1080837-c663-4cbe-9951-7b18c766e54a',
                            'bk_client_context':
                                '{"bloks_version":"0ee04a4a6556c5bb584487d649442209a3ae880ae5c6380b16235b870fcc4052","styles_id":"instagram"}',
                            'bloks_versioning_id':
                                '0ee04a4a6556c5bb584487d649442209a3ae880ae5c6380b16235b870fcc4052',
                        }
                        req = requests.post('https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.instagram_bloks_bottom_sheet.ixt.screen.frx_policy_education/',data=data,headers=headers)
                        context = re.search(r', \"serialized_state\", \"INTERNAL__latency_qpl_marker_id\", \"INTERNAL__latency_qpl_instance_id\"\), \(bk.action.array.Make, \"(.*?)\", ',str(req.json())).group(1)
                        data = {
                            'params':
                                '{"server_params":{"serialized_state":"'+context+'","INTERNAL__latency_qpl_marker_id":36707139,"INTERNAL__latency_qpl_instance_id":57138440800005}}',
                            '_uuid': 'b1080837-c663-4cbe-9951-7b18c766e54a',
                            'bk_client_context':
                                '{"bloks_version":"0ee04a4a6556c5bb584487d649442209a3ae880ae5c6380b16235b870fcc4052","styles_id":"instagram"}',
                            'bloks_versioning_id':
                                '0ee04a4a6556c5bb584487d649442209a3ae880ae5c6380b16235b870fcc4052',
                        }
                        req = requests.post('https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.instagram_bloks_bottom_sheet.ixt.screen.frx_post_report_process_timeline/',data=data,headers=headers)
                        if req.text.__contains__('"status":"ok"'):
                            self.done += 1
                        else:
                            self.error += 1

                    elif self.report_type == 3:

                        data = {
                            'params':
                                '{"client_input_params":{"tags":["ig_hate_speech_v3","ig_its_inappropriate"]},"server_params":{"show_tag_search":0,"serialized_state":"'+context+'","INTERNAL__latency_qpl_marker_id":36707139,"INTERNAL__latency_qpl_instance_id":61259265200231,"is_bloks":1,"tag_source":"tag_selection_screen"}}',
                            '_uuid': 'b1080837-c663-4cbe-9951-7b18c766e54a',
                            'bk_client_context':
                                '{"bloks_version":"0ee04a4a6556c5bb584487d649442209a3ae880ae5c6380b16235b870fcc4052","styles_id":"instagram"}',
                            'bloks_versioning_id':
                                '0ee04a4a6556c5bb584487d649442209a3ae880ae5c6380b16235b870fcc4052',
                        }
                        req = requests.post('https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.instagram_bloks_bottom_sheet.ixt.screen.frx_tag_selection_screen/',data=data,headers=headers)
                        context = re.search(r'\"report\", \"(.*?)\", ',str(req.json())).group(1)
                        data = {
                            'params':
                                '{"server_params":{"serialized_state":"'+context+'","INTERNAL__latency_qpl_marker_id":36707139,"INTERNAL__latency_qpl_instance_id":57131417800002,"selected_option":"report"}}',
                            '_uuid': 'b1080837-c663-4cbe-9951-7b18c766e54a',
                            'bk_client_context':
                                '{"bloks_version":"0ee04a4a6556c5bb584487d649442209a3ae880ae5c6380b16235b870fcc4052","styles_id":"instagram"}',
                            'bloks_versioning_id':
                                '0ee04a4a6556c5bb584487d649442209a3ae880ae5c6380b16235b870fcc4052',
                        }
                        req = requests.post('https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.instagram_bloks_bottom_sheet.ixt.screen.frx_policy_education/',data=data,headers=headers)
                        context = re.search(r', \"serialized_state\", \"INTERNAL__latency_qpl_marker_id\", \"INTERNAL__latency_qpl_instance_id\"\), \(bk.action.array.Make, \"(.*?)\", ',str(req.json())).group(1)
                        data = {
                            'params':
                                '{"server_params":{"serialized_state":"'+context+'","INTERNAL__latency_qpl_marker_id":36707139,"INTERNAL__latency_qpl_instance_id":57138440800005}}',
                            '_uuid': 'b1080837-c663-4cbe-9951-7b18c766e54a',
                            'bk_client_context':
                                '{"bloks_version":"0ee04a4a6556c5bb584487d649442209a3ae880ae5c6380b16235b870fcc4052","styles_id":"instagram"}',
                            'bloks_versioning_id':
                                '0ee04a4a6556c5bb584487d649442209a3ae880ae5c6380b16235b870fcc4052',
                        }
                        req = requests.post('https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.instagram_bloks_bottom_sheet.ixt.screen.frx_post_report_process_timeline/',data=data,headers=headers)
                        if req.text.__contains__('"status":"ok"'):
                            self.done += 1
                        else:
                            self.error += 1

                    elif self.report_type == 4:
                        data = {
                            'params':
                                '{"client_input_params":{"tags":["ig_violence_parent","ig_report_account","ig_its_inappropriate"]},"server_params":{"show_tag_search":0,"serialized_state":"'+context+'","INTERNAL__latency_qpl_marker_id":36707139,"INTERNAL__latency_qpl_instance_id":71565967300275,"is_bloks":1,"tag_source":"tag_selection_screen"}}',
                            '_uuid': 'b1080837-c663-4cbe-9951-7b18c766e54a',
                            'bk_client_context':
                                '{"bloks_version":"0ee04a4a6556c5bb584487d649442209a3ae880ae5c6380b16235b870fcc4052","styles_id":"instagram"}',
                            'bloks_versioning_id':
                                '0ee04a4a6556c5bb584487d649442209a3ae880ae5c6380b16235b870fcc4052',
                        }
                        req = requests.post('https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.instagram_bloks_bottom_sheet.ixt.screen.frx_tag_selection_screen/',data=data,headers=headers)
                        context = re.search(r'"tag_selection_screen\", \"(.*?)\", ',str(req.json())).group(1)
                        data = {
                            'params':
                                '{"client_input_params":{"tags":["ig_violence_threat","ig_report_account","ig_its_inappropriate","ig_violence_parent"]},"server_params":{"show_tag_search":0,"serialized_state":"'+context+'","INTERNAL__latency_qpl_marker_id":36707139,"INTERNAL__latency_qpl_instance_id":71607815700034,"is_bloks":1,"tag_source":"tag_selection_screen"}}',
                            '_uuid': 'b1080837-c663-4cbe-9951-7b18c766e54a',
                            'bk_client_context':
                                '{"bloks_version":"0ee04a4a6556c5bb584487d649442209a3ae880ae5c6380b16235b870fcc4052","styles_id":"instagram"}',
                            'bloks_versioning_id':
                                '0ee04a4a6556c5bb584487d649442209a3ae880ae5c6380b16235b870fcc4052',
                        }
                        req = requests.post('https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.instagram_bloks_bottom_sheet.ixt.screen.frx_tag_selection_screen/',data=data,headers=headers)
                        context = re.search(r'\(bk.action.array.Make, \(bk.action.i32.Const, -1\), \"(.*?)\", ',str(req.json())).group(1)
                        data = {
                            'params':
                                '{"server_params":{"serialized_state":"'+context+'","INTERNAL__latency_qpl_marker_id":36707139,"INTERNAL__latency_qpl_instance_id":57131417800002,"selected_option":"report"}}',
                            '_uuid': 'b1080837-c663-4cbe-9951-7b18c766e54a',
                            'bk_client_context':
                                '{"bloks_version":"0ee04a4a6556c5bb584487d649442209a3ae880ae5c6380b16235b870fcc4052","styles_id":"instagram"}',
                            'bloks_versioning_id':
                                '0ee04a4a6556c5bb584487d649442209a3ae880ae5c6380b16235b870fcc4052',
                        }
                        req = requests.post('https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.instagram_bloks_bottom_sheet.ixt.screen.frx_policy_education/',data=data,headers=headers)
                        context = re.search(r', \"serialized_state\", \"INTERNAL__latency_qpl_marker_id\", \"INTERNAL__latency_qpl_instance_id\"\), \(bk.action.array.Make, \"(.*?)\", ',str(req.json())).group(1)
                        data = {
                            'params':
                                '{"server_params":{"serialized_state":"'+context+'","INTERNAL__latency_qpl_marker_id":36707139,"INTERNAL__latency_qpl_instance_id":57138440800005}}',
                            '_uuid': 'b1080837-c663-4cbe-9951-7b18c766e54a',
                            'bk_client_context':
                                '{"bloks_version":"0ee04a4a6556c5bb584487d649442209a3ae880ae5c6380b16235b870fcc4052","styles_id":"instagram"}',
                            'bloks_versioning_id':
                                '0ee04a4a6556c5bb584487d649442209a3ae880ae5c6380b16235b870fcc4052',
                        }
                        req = requests.post('https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.instagram_bloks_bottom_sheet.ixt.screen.frx_post_report_process_timeline/',data=data,headers=headers)
                        if req.text.__contains__('"status":"ok"'):
                            self.done += 1
                        else:
                            self.error += 1

                    elif self.report_type == 5:
                        data = {
                            'params':
                                '{"client_input_params":{"tags":["ig_nudity_v2","ig_report_account","ig_its_inappropriate"]},"server_params":{"show_tag_search":0,"serialized_state":"'+context+'","INTERNAL__latency_qpl_marker_id":36707139,"INTERNAL__latency_qpl_instance_id":74299849900199,"is_bloks":1,"tag_source":"tag_selection_screen"}}',
                            '_uuid': 'b1080837-c663-4cbe-9951-7b18c766e54a',
                            'bk_client_context':
                                '{"bloks_version":"0ee04a4a6556c5bb584487d649442209a3ae880ae5c6380b16235b870fcc4052","styles_id":"instagram"}',
                            'bloks_versioning_id':
                                '0ee04a4a6556c5bb584487d649442209a3ae880ae5c6380b16235b870fcc4052',
                        }
                        req = requests.post('https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.instagram_bloks_bottom_sheet.ixt.screen.frx_tag_selection_screen/',data=data,headers=headers)
                        context = re.search(r'"tag_selection_screen\", \"(.*?)\", ',str(req.json())).group(1)
                        data = {
                            'params':
                                '{"client_input_params":{"tags":["ig_nudity_or_pornography_v3","ig_report_account","ig_its_inappropriate","ig_nudity_v2"]},"server_params":{"show_tag_search":0,"serialized_state":"'+context+'","INTERNAL__latency_qpl_marker_id":36707139,"INTERNAL__latency_qpl_instance_id":74315612200034,"is_bloks":1,"tag_source":"tag_selection_screen"}}',
                            '_uuid': 'b1080837-c663-4cbe-9951-7b18c766e54a',
                            'bk_client_context':
                                '{"bloks_version":"0ee04a4a6556c5bb584487d649442209a3ae880ae5c6380b16235b870fcc4052","styles_id":"instagram"}',
                            'bloks_versioning_id':
                                '0ee04a4a6556c5bb584487d649442209a3ae880ae5c6380b16235b870fcc4052',
                        }
                        req = requests.post('https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.instagram_bloks_bottom_sheet.ixt.screen.frx_tag_selection_screen/',data=data,headers=headers)
                        context = re.search(r'\(bk.action.array.Make, \(bk.action.i32.Const, -1\), \"(.*?)\", ',str(req.json())).group(1)
                        data = {
                            'params':
                                '{"server_params":{"serialized_state":"'+context+'","INTERNAL__latency_qpl_marker_id":36707139,"INTERNAL__latency_qpl_instance_id":57131417800002,"selected_option":"report"}}',
                            '_uuid': 'b1080837-c663-4cbe-9951-7b18c766e54a',
                            'bk_client_context':
                                '{"bloks_version":"0ee04a4a6556c5bb584487d649442209a3ae880ae5c6380b16235b870fcc4052","styles_id":"instagram"}',
                            'bloks_versioning_id':
                                '0ee04a4a6556c5bb584487d649442209a3ae880ae5c6380b16235b870fcc4052',
                        }
                        req = requests.post('https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.instagram_bloks_bottom_sheet.ixt.screen.frx_policy_education/',data=data,headers=headers)
                        context = re.search(r', \"serialized_state\", \"INTERNAL__latency_qpl_marker_id\", \"INTERNAL__latency_qpl_instance_id\"\), \(bk.action.array.Make, \"(.*?)\", ',str(req.json())).group(1)
                        data = {
                            'params':
                                '{"server_params":{"serialized_state":"'+context+'","INTERNAL__latency_qpl_marker_id":36707139,"INTERNAL__latency_qpl_instance_id":57138440800005}}',
                            '_uuid': 'b1080837-c663-4cbe-9951-7b18c766e54a',
                            'bk_client_context':
                                '{"bloks_version":"0ee04a4a6556c5bb584487d649442209a3ae880ae5c6380b16235b870fcc4052","styles_id":"instagram"}',
                            'bloks_versioning_id':
                                '0ee04a4a6556c5bb584487d649442209a3ae880ae5c6380b16235b870fcc4052',
                        }
                        req = requests.post('https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.instagram_bloks_bottom_sheet.ixt.screen.frx_post_report_process_timeline/',data=data,headers=headers)
                        if req.text.__contains__('"status":"ok"'):
                            self.done += 1
                        else:
                            self.error += 1
                            
                    elif self.report_type == 6:
                        data = {
                            'params':
                                '{"client_input_params":{"tags":["ig_bullying_or_harassment_comment_v3","ig_report_account","ig_its_inappropriate"]},"server_params":{"show_tag_search":0,"serialized_state":"'+context+'","INTERNAL__latency_qpl_marker_id":36707139,"INTERNAL__latency_qpl_instance_id":72669687400313,"is_bloks":1,"tag_source":"tag_selection_screen"}}',
                            '_uuid': 'b1080837-c663-4cbe-9951-7b18c766e54a',
                            'bk_client_context':
                                '{"bloks_version":"0ee04a4a6556c5bb584487d649442209a3ae880ae5c6380b16235b870fcc4052","styles_id":"instagram"}',
                            'bloks_versioning_id':
                                '0ee04a4a6556c5bb584487d649442209a3ae880ae5c6380b16235b870fcc4052',
                        }
                        req = requests.post('https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.instagram_bloks_bottom_sheet.ixt.screen.frx_tag_selection_screen/',data=data,headers=headers)
                        context = re.search(r'"tag_selection_screen\", \"(.*?)\", ',str(req.json())).group(1)
                        data = {
                            'params':
                                '{"client_input_params":{"tags":["ig_bullying_or_harassment_me_v3","ig_report_account","ig_its_inappropriate","ig_bullying_or_harassment_comment_v3"]},"server_params":{"show_tag_search":0,"serialized_state":"'+context+'","INTERNAL__latency_qpl_marker_id":36707139,"INTERNAL__latency_qpl_instance_id":72799402900047,"is_bloks":1,"tag_source":"tag_selection_screen"}}',
                            '_uuid': 'b1080837-c663-4cbe-9951-7b18c766e54a',
                            'bk_client_context':
                                '{"bloks_version":"0ee04a4a6556c5bb584487d649442209a3ae880ae5c6380b16235b870fcc4052","styles_id":"instagram"}',
                            'bloks_versioning_id':
                                '0ee04a4a6556c5bb584487d649442209a3ae880ae5c6380b16235b870fcc4052',
                        }
                        req = requests.post('https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.instagram_bloks_bottom_sheet.ixt.screen.frx_tag_selection_screen/',data=data,headers=headers)
                        context = re.search(r'\"report\", \"(.*?)\", ',str(req.json())).group(1)
                        data = {
                            'params':
                                '{"server_params":{"serialized_state":"'+context+'","INTERNAL__latency_qpl_marker_id":36707139,"INTERNAL__latency_qpl_instance_id":57131417800002,"selected_option":"report"}}',
                            '_uuid': 'b1080837-c663-4cbe-9951-7b18c766e54a',
                            'bk_client_context':
                                '{"bloks_version":"0ee04a4a6556c5bb584487d649442209a3ae880ae5c6380b16235b870fcc4052","styles_id":"instagram"}',
                            'bloks_versioning_id':
                                '0ee04a4a6556c5bb584487d649442209a3ae880ae5c6380b16235b870fcc4052',
                        }
                        req = requests.post('https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.instagram_bloks_bottom_sheet.ixt.screen.frx_policy_education/',data=data,headers=headers)
                        context = re.search(r', \"serialized_state\", \"INTERNAL__latency_qpl_marker_id\", \"INTERNAL__latency_qpl_instance_id\"\), \(bk.action.array.Make, \"(.*?)\", ',str(req.json())).group(1)
                        data = {
                            'params':
                                '{"server_params":{"serialized_state":"'+context+'","INTERNAL__latency_qpl_marker_id":36707139,"INTERNAL__latency_qpl_instance_id":57138440800005}}',
                            '_uuid': 'b1080837-c663-4cbe-9951-7b18c766e54a',
                            'bk_client_context':
                                '{"bloks_version":"0ee04a4a6556c5bb584487d649442209a3ae880ae5c6380b16235b870fcc4052","styles_id":"instagram"}',
                            'bloks_versioning_id':
                                '0ee04a4a6556c5bb584487d649442209a3ae880ae5c6380b16235b870fcc4052',
                        }
                        req = requests.post('https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.instagram_bloks_bottom_sheet.ixt.screen.frx_post_report_process_timeline/',data=data,headers=headers)
                        if req.text.__contains__('"status":"ok"'):
                            self.done += 1
                        else:
                            self.error += 1
                    elif self.report_type == 7:
                        data = {
                            'params':
                                '{"client_input_params":{"tags":["ig_sale_of_illegal_or_regulated_goods_v3","ig_its_inappropriate"]},"server_params":{"show_tag_search":0,"serialized_state":"'+context+'","INTERNAL__latency_qpl_marker_id":36707139,"INTERNAL__latency_qpl_instance_id":62179084800155,"is_bloks":1,"tag_source":"tag_selection_screen"}}',
                            '_uuid': 'b1080837-c663-4cbe-9951-7b18c766e54a',
                            'bk_client_context':
                                '{"bloks_version":"0ee04a4a6556c5bb584487d649442209a3ae880ae5c6380b16235b870fcc4052","styles_id":"instagram"}',
                            'bloks_versioning_id':
                                '0ee04a4a6556c5bb584487d649442209a3ae880ae5c6380b16235b870fcc4052',
                        }
                        req = requests.post('https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.instagram_bloks_bottom_sheet.ixt.screen.frx_tag_selection_screen/',data=data,headers=headers)
                        context = re.search(r'"tag_selection_screen\", \"(.*?)\", ',str(req.json())).group(1)
                        data = {
                            'params':
                                '{"client_input_params":{"tags":["ig_drugs_v3","ig_its_inappropriate","ig_sale_of_illegal_or_regulated_goods_v3"]},"server_params":{"show_tag_search":0,"serialized_state":"'+context+'","INTERNAL__latency_qpl_marker_id":36707139,"INTERNAL__latency_qpl_instance_id":62216886700074,"is_bloks":1,"tag_source":"tag_selection_screen"}}',
                            '_uuid': 'b1080837-c663-4cbe-9951-7b18c766e54a',
                            'bk_client_context':
                                '{"bloks_version":"0ee04a4a6556c5bb584487d649442209a3ae880ae5c6380b16235b870fcc4052","styles_id":"instagram"}',
                            'bloks_versioning_id':
                                '0ee04a4a6556c5bb584487d649442209a3ae880ae5c6380b16235b870fcc4052',
                        }
                        req = requests.post('https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.instagram_bloks_bottom_sheet.ixt.screen.frx_tag_selection_screen/',data=data,headers=headers)
                        context = re.search(r'\(bk.action.array.Make, \(bk.action.i32.Const, -1\), \"(.*?)\", ',str(req.json())).group(1)
                        data = {
                            'params':
                                '{"server_params":{"serialized_state":"'+context+'","INTERNAL__latency_qpl_marker_id":36707139,"INTERNAL__latency_qpl_instance_id":57131417800002,"selected_option":"report"}}',
                            '_uuid': 'b1080837-c663-4cbe-9951-7b18c766e54a',
                            'bk_client_context':
                                '{"bloks_version":"0ee04a4a6556c5bb584487d649442209a3ae880ae5c6380b16235b870fcc4052","styles_id":"instagram"}',
                            'bloks_versioning_id':
                                '0ee04a4a6556c5bb584487d649442209a3ae880ae5c6380b16235b870fcc4052',
                        }
                        req = requests.post('https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.instagram_bloks_bottom_sheet.ixt.screen.frx_policy_education/',data=data,headers=headers)
                        context = re.search(r', \"serialized_state\", \"INTERNAL__latency_qpl_marker_id\", \"INTERNAL__latency_qpl_instance_id\"\), \(bk.action.array.Make, \"(.*?)\", ',str(req.json())).group(1)
                        data = {
                            'params':
                                '{"server_params":{"serialized_state":"'+context+'","INTERNAL__latency_qpl_marker_id":36707139,"INTERNAL__latency_qpl_instance_id":57138440800005}}',
                            '_uuid': 'b1080837-c663-4cbe-9951-7b18c766e54a',
                            'bk_client_context':
                                '{"bloks_version":"0ee04a4a6556c5bb584487d649442209a3ae880ae5c6380b16235b870fcc4052","styles_id":"instagram"}',
                            'bloks_versioning_id':
                                '0ee04a4a6556c5bb584487d649442209a3ae880ae5c6380b16235b870fcc4052',
                        }
                        req = requests.post('https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.instagram_bloks_bottom_sheet.ixt.screen.frx_post_report_process_timeline/',data=data,headers=headers)
                        if req.text.__contains__('"status":"ok"'):
                            self.done += 1
                        else:
                            self.error += 1
                except:
                   self.error += 1 
                
                print(f" {Fore.LIGHTCYAN_EX}[ {Fore.LIGHTWHITE_EX}Done : {Fore.LIGHTGREEN_EX}{self.done} {Fore.LIGHTWHITE_EX}, {Fore.LIGHTWHITE_EX}Errors : {Fore.RED}{self.error} {Fore.LIGHTCYAN_EX}]", end='\r')

                time.sleep(self.sleep)

    def get_stories(self):
        headers = {
        'X-IG-App-Locale': 'en_US',
        'X-IG-Device-Locale': 'en_US',
        'X-IG-Mapped-Locale': 'en_US',
        'X-IG-Connection-Type': 'WIFI',
        'X-IG-Capabilities': '3brTvw8=',
        'User-Agent':
            'Instagram 148.0.0.33.121 Android (28/9; 480dpi; 1080x2137; HUAWEI; JKM-LX1; HWJKM-H; kirin710; en_US; 216817344)',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'i.instagram.com',
        'Cookie': f'sessionid={self.cookies[0]}'
        }
        req = requests.get(f'https://i.instagram.com/api/v1/feed/user/{self.user_id}/story/',headers=headers)

        try:
            for story in req.json()["reel"]['items']:
                self.stories.append(str(story['id']))
        except:
            print("[ X ] No stories found enter to exit ...")
            input()
            exit()

    def report_stories(self):
        while True:
            for cookie in self.cookies:
                for storyId in self.stories:
                    try:
                        headers = {
                        'Host': 'i.instagram.com',
                        'X-Ig-App-Locale': 'en_US',
                        'X-Ig-Device-Locale': 'en_US',
                        'X-Ig-Mapped-Locale': 'en_US',
                        'X-Pigeon-Session-Id': 'UFS-0e5afa95-b45f-4aa8-af41-9e039533d67b-0',
                        'X-Pigeon-Rawclienttime': '1678118511.889',
                        'X-Ig-Bandwidth-Speed-Kbps': '3828.000',
                        'X-Ig-Bandwidth-Totalbytes-B': '3185285',
                        'X-Ig-Bandwidth-Totaltime-Ms': '572',
                        'X-Ig-App-Startup-Country': 'IQ',
                        'X-Ig-Nav-Chain':
                            'MainFeedFragment:feed_timeline:1:cold_start:1678895074.82:69#230#301:3057819701217259875,ReelViewerFragment:reel_feed_timeline_item_header:2:button:1678895096.14::,EmptyReportBottomSheetFragment:empty_report_bottom_sheet_fragment:3:button:1678895105.20::,IgBloksBottomSheetFragment:bloks_unknown:4:button:1678895105.623::,ReelViewerFragment:reel_feed_timeline_item_header:5:warm_start:1678895497.503::,IgBloksBottomSheetFragment:bloks_unknown:6:button:1678895497.523::,IgBloksBottomSheetFragmen',
                        'X-Bloks-Version-Id':
                            '0ee04a4a6556c5bb584487d649442209a3ae880ae5c6380b16235b870fcc4052',
                        'X-Ig-Www-Claim': 'hmac.AR1aWEsDw6WfWexHDkfbg_-temKojpBG0NZXzjGWwnoWouO9',
                        'X-Bloks-Is-Layout-Rtl': 'false',
                        'X-Ig-Device-Id': '59579ca5-e663-4fee-b090-e8fcc8f193f3',
                        'X-Ig-Family-Device-Id': 'e921fc15-0499-46dc-943d-3350f6b3fa02',
                        'X-Ig-Android-Id': 'android-f2e05b426b619b1b',
                        'X-Ig-Timezone-Offset': '10800',
                        'User-Agent':
                            'Instagram 265.0.0.19.301 Android (30/11; 420dpi; 1080x1794; Google/google; sdk_gphone_x86; generic_x86_arm; ranchu; en_US; 436384447)',
                        'Accept-Language': 'en-US',
                        'Cookie':f'sessionid={cookie}',
                        'X-Mid': 'ZAYOQQABAAGyslKmLdaVOc4U-ScJ',
                        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                        }
                        data = {
                        'logging_extra':
                            '{"reporting_timestamp":"1678873425","navigation_chain":"MainFeedFragment:feed_timeline:1:cold_start:1678809945.209:10#230#301:3057819701217259875,UserDetailFragment:profile:2:media_owner:1678810005.579::,ProfileMediaTabFragment:profile:3:button:1678810006.516::,ReelViewerFragment:reel_profile:4:button:1678810016.828::"}',
                        'trigger_event_type': 'ig_report_button_clicked',
                        'trigger_session_id': '7984e61d-72db-4f92-83fc-64c74da14d62',
                        'ig_container_module': 'reel_profile',
                        'entry_point': 'chevron_button',
                        'preloading_enabled': '1',
                        '_uuid': '3ae08b3b-5663-48eb-88af-30364bc3201e',
                        'ig_object_value': storyId,
                        'ig_object_type': '1',
                        'bk_client_context':
                            '{"bloks_version":"0ee04a4a6556c5bb584487d649442209a3ae880ae5c6380b16235b870fcc4052","styles_id":"instagram"}',
                        'ixt_initial_screen_id': '7f6b007c-94e8-4d25-b7f9-e363e9776f0f',
                        'bloks_versioning_id':
                            '0ee04a4a6556c5bb584487d649442209a3ae880ae5c6380b16235b870fcc4052',
                        'location': 'ig_story',
                        }
                        req = requests.post('https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.ig.ixt.triggers.bottom_sheet.ig_content/',headers=headers,data=data)
                        context = re.search(r', \"tag_selection_screen\", \"(.*?)\", ',str(req.json())).group(1)
                        if self.report_type == 1:
                            data = {
                                'params':
                                    '{"client_input_params":{"tags":["ig_spam_v3"]},"server_params":{"show_tag_search":1,"serialized_state":"'+context+'","INTERNAL__latency_qpl_marker_id":36707139,"INTERNAL__latency_qpl_instance_id":98937914900072,"is_bloks":1,"tag_source":"tag_selection_screen"}}',
                                '_uuid': '3ae08b3b-5663-48eb-88af-30364bc3201e',
                                'bk_client_context':
                                    '{"bloks_version":"0ee04a4a6556c5bb584487d649442209a3ae880ae5c6380b16235b870fcc4052","styles_id":"instagram"}',
                                'bloks_versioning_id':
                                    '0ee04a4a6556c5bb584487d649442209a3ae880ae5c6380b16235b870fcc4052',
                            }
                            req = requests.post('https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.instagram_bloks_bottom_sheet.ixt.screen.frx_tag_selection_screen/',headers=headers,data=data)
                            context = re.search(r'\"INTERNAL__latency_qpl_marker_id\", \"INTERNAL__latency_qpl_instance_id\"\), \(bk.action.array.Make, \"(.*?)\", ',str(req.json())).group(1)
                            data = {
                                'params':
                                    '{"server_params":{"serialized_state":"'+context+'","INTERNAL__latency_qpl_marker_id":36707139,"INTERNAL__latency_qpl_instance_id":99266571600005}}',
                                '_uuid': '3ae08b3b-5663-48eb-88af-30364bc3201e',
                                'bk_client_context':
                                    '{"bloks_version":"0ee04a4a6556c5bb584487d649442209a3ae880ae5c6380b16235b870fcc4052","styles_id":"instagram"}',
                                'bloks_versioning_id':
                                    '0ee04a4a6556c5bb584487d649442209a3ae880ae5c6380b16235b870fcc4052',
                            }
                            req = requests.post('https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.instagram_bloks_bottom_sheet.ixt.screen.frx_post_report_process_timeline/',data=data,headers=headers)
                            if req.text.__contains__('"status":"ok"'):
                                self.done += 1
                            else:
                                self.error += 1

                        elif self.report_type == 2:
                            data = {
                                'params':
                                    '{"client_input_params":{"tags":["ig_self_injury_v3"]},"server_params":{"show_tag_search":1,"serialized_state":"'+context+'","INTERNAL__latency_qpl_marker_id":36707139,"INTERNAL__latency_qpl_instance_id":100286078000148,"is_bloks":1,"tag_source":"tag_selection_screen"}}',
                                '_uuid': '2c914a68-0663-4801-b145-88cfba3e9151',
                                'bk_client_context':
                                    '{"bloks_version":"0ee04a4a6556c5bb584487d649442209a3ae880ae5c6380b16235b870fcc4052","styles_id":"instagram"}',
                                'bloks_versioning_id':
                                    '0ee04a4a6556c5bb584487d649442209a3ae880ae5c6380b16235b870fcc4052',
                            }
                            req = requests.post('https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.instagram_bloks_bottom_sheet.ixt.screen.frx_tag_selection_screen/',headers=headers,data=data)
                            context = re.search(r' \"report\", \"(.*?)\", ',str(req.json())).group(1)
                            data = {
                                'params':
                                    '{"server_params":{"serialized_state":"'+context+'","INTERNAL__latency_qpl_marker_id":36707139,"INTERNAL__latency_qpl_instance_id":182710706400002,"selected_option":"report"}}',
                                '_uuid': 'e5c7c347-a663-40ea-a015-b1b4e7a548a0',
                                'bk_client_context':
                                    '{"bloks_version":"0ee04a4a6556c5bb584487d649442209a3ae880ae5c6380b16235b870fcc4052","styles_id":"instagram"}',
                                'bloks_versioning_id':
                                    '0ee04a4a6556c5bb584487d649442209a3ae880ae5c6380b16235b870fcc4052',
                            }
                            req = requests.post('https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.instagram_bloks_bottom_sheet.ixt.screen.frx_policy_education/',headers=headers,data=data)
                            context = re.search(r', \"serialized_state\", \"INTERNAL__latency_qpl_marker_id\", \"INTERNAL__latency_qpl_instance_id\"\), \(bk.action.array.Make, \"(.*?)\",',str(req.json())).group(1)
                            data = {
                                'params':
                                    '{"server_params":{"serialized_state":"'+context+'","INTERNAL__latency_qpl_marker_id":36707139,"INTERNAL__latency_qpl_instance_id":188069605300005}}',
                                '_uuid': 'f0b0f75c-e663-4a21-a74d-2680b832c712',
                                'bk_client_context':
                                    '{"bloks_version":"0ee04a4a6556c5bb584487d649442209a3ae880ae5c6380b16235b870fcc4052","styles_id":"instagram"}',
                                'bloks_versioning_id':
                                    '0ee04a4a6556c5bb584487d649442209a3ae880ae5c6380b16235b870fcc4052',
                            }
                            req = requests.post('https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.instagram_bloks_bottom_sheet.ixt.screen.frx_post_report_process_timeline/',data=data,headers=headers)
                            if req.text.__contains__('"status":"ok"'):
                                self.done += 1
                            else:
                                self.error += 1
                        elif self.report_type == 3:
                            data = {
                                'params':
                                    '{"client_input_params":{"tags":["ig_hate_speech_v3"]},"server_params":{"show_tag_search":1,"serialized_state":"'+context+'","INTERNAL__latency_qpl_marker_id":36707139,"INTERNAL__latency_qpl_instance_id":100442209200110,"is_bloks":1,"tag_source":"tag_selection_screen"}}',
                                '_uuid': '3ae08b3b-5663-48eb-88af-30364bc3201e',
                                'bk_client_context':
                                    '{"bloks_version":"0ee04a4a6556c5bb584487d649442209a3ae880ae5c6380b16235b870fcc4052","styles_id":"instagram"}',
                                'bloks_versioning_id':
                                    '0ee04a4a6556c5bb584487d649442209a3ae880ae5c6380b16235b870fcc4052',
                            }
                            req = requests.post('https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.instagram_bloks_bottom_sheet.ixt.screen.frx_tag_selection_screen/',headers=headers,data=data)
                            context = re.search(r' \"report\", \"(.*?)\", ',str(req.json())).group(1)
                            data = {
                                'params':
                                    '{"server_params":{"serialized_state":"'+context+'","INTERNAL__latency_qpl_marker_id":36707139,"INTERNAL__latency_qpl_instance_id":100462249300002,"selected_option":"report"}}',
                                '_uuid': '3ae08b3b-5663-48eb-88af-30364bc3201e',
                                'bk_client_context':
                                    '{"bloks_version":"0ee04a4a6556c5bb584487d649442209a3ae880ae5c6380b16235b870fcc4052","styles_id":"instagram"}',
                                'bloks_versioning_id':
                                    '0ee04a4a6556c5bb584487d649442209a3ae880ae5c6380b16235b870fcc4052',
                            }
                            req = requests.post('https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.instagram_bloks_bottom_sheet.ixt.screen.frx_policy_education/',headers=headers,data=data)
                            context = re.search(r', \"serialized_state\", \"INTERNAL__latency_qpl_marker_id\", \"INTERNAL__latency_qpl_instance_id\"\), \(bk.action.array.Make, \"(.*?)\",',str(req.json())).group(1)
                            data = {
                                'params':
                                    '{"server_params":{"serialized_state":"'+context+'","INTERNAL__latency_qpl_marker_id":36707139,"INTERNAL__latency_qpl_instance_id":101179220200005}}',
                                '_uuid': '3ae08b3b-5663-48eb-88af-30364bc3201e',
                                'bk_client_context':
                                    '{"bloks_version":"0ee04a4a6556c5bb584487d649442209a3ae880ae5c6380b16235b870fcc4052","styles_id":"instagram"}',
                                'bloks_versioning_id':
                                    '0ee04a4a6556c5bb584487d649442209a3ae880ae5c6380b16235b870fcc4052',
                            }
                            req = requests.post('https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.instagram_bloks_bottom_sheet.ixt.screen.frx_post_report_process_timeline/',data=data,headers=headers)
                            if req.text.__contains__('"status":"ok"'):
                                self.done += 1
                            else:
                                self.error += 1
                        #[ 1 ] Spam\n[ 2 ] Self\n[ 3 ] Hate\n[ 4 ] Violence\n[ 5 ] Nudity\n[ 6 ] Bullying\n[ 7 ] Drugs
                        elif self.report_type == 4:
                            data = {
                                'params':
                                    '{"client_input_params":{"tags":["ig_violence_parent"]},"server_params":{"show_tag_search":1,"serialized_state":"'+context+'","INTERNAL__latency_qpl_marker_id":36707139,"INTERNAL__latency_qpl_instance_id":102159124600186,"is_bloks":1,"tag_source":"tag_selection_screen"}}',
                                '_uuid': '3ae08b3b-5663-48eb-88af-30364bc3201e',
                                'bk_client_context':
                                    '{"bloks_version":"0ee04a4a6556c5bb584487d649442209a3ae880ae5c6380b16235b870fcc4052","styles_id":"instagram"}',
                                'bloks_versioning_id':
                                    '0ee04a4a6556c5bb584487d649442209a3ae880ae5c6380b16235b870fcc4052',
                            }
                            req = requests.post('https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.instagram_bloks_bottom_sheet.ixt.screen.frx_tag_selection_screen/',data=data,headers=headers)
                            context = re.search(r'\"tag_selection_screen\", \"(.*?)\", ',str(req.json())).group(1)
                            data = {
                                'params':
                                    '{"client_input_params":{"tags":["ig_violence_threat","ig_violence_parent"]},"server_params":{"show_tag_search":1,"serialized_state":"'+context+'","INTERNAL__latency_qpl_marker_id":36707139,"INTERNAL__latency_qpl_instance_id":102164812700034,"is_bloks":1,"tag_source":"tag_selection_screen"}}',
                                '_uuid': '3ae08b3b-5663-48eb-88af-30364bc3201e',
                                'bk_client_context':
                                    '{"bloks_version":"0ee04a4a6556c5bb584487d649442209a3ae880ae5c6380b16235b870fcc4052","styles_id":"instagram"}',
                                'bloks_versioning_id':
                                    '0ee04a4a6556c5bb584487d649442209a3ae880ae5c6380b16235b870fcc4052',
                            }
                            req = requests.post('https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.instagram_bloks_bottom_sheet.ixt.screen.frx_tag_selection_screen/',data=data,headers=headers)
                            context = re.search(r'\(bk.action.array.Make, \(bk.action.i32.Const, -1\), \"(.*?)\", ',str(req.json())).group(1)
                            data = {
                                'params':
                                    '{"server_params":{"channel":-1,"serialized_state":"'+context+'","INTERNAL__latency_qpl_marker_id":36707139,"INTERNAL__latency_qpl_instance_id":102636218000006}}',
                                '_uuid': '3ae08b3b-5663-48eb-88af-30364bc3201e',
                                'bk_client_context':
                                    '{"bloks_version":"0ee04a4a6556c5bb584487d649442209a3ae880ae5c6380b16235b870fcc4052","styles_id":"instagram"}',
                                'bloks_versioning_id':
                                    '0ee04a4a6556c5bb584487d649442209a3ae880ae5c6380b16235b870fcc4052',
                            }
                            req = requests.post('https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.instagram_bloks_bottom_sheet.ixt.screen.frx_report_review_screen/',data=data,headers=headers)
                            context = re.search(r' \"serialized_state\", \"INTERNAL__latency_qpl_marker_id\", \"INTERNAL__latency_qpl_instance_id\"\), \(bk.action.array.Make, \"(.*?)\", ',str(req.json())).group(1)
                            data = {
                                'params':
                                    '{"server_params":{"serialized_state":"'+context+'","INTERNAL__latency_qpl_marker_id":36707139,"INTERNAL__latency_qpl_instance_id":103086232600005}}',
                                '_uuid': '3ae08b3b-5663-48eb-88af-30364bc3201e',
                                'bk_client_context':
                                    '{"bloks_version":"0ee04a4a6556c5bb584487d649442209a3ae880ae5c6380b16235b870fcc4052","styles_id":"instagram"}',
                                'bloks_versioning_id':
                                    '0ee04a4a6556c5bb584487d649442209a3ae880ae5c6380b16235b870fcc4052',
                            }
                            req = requests.post('https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.instagram_bloks_bottom_sheet.ixt.screen.frx_post_report_process_timeline/',data=data,headers=headers)
                            if req.text.__contains__('"status":"ok"'):
                                self.done += 1
                            else:
                                self.error += 1
                        
                        elif self.report_type == 5:
                            data = {
                                'params':
                                    '{"client_input_params":{"tags":["ig_nudity_v2"]},"server_params":{"show_tag_search":1,"serialized_state":"'+context+'","INTERNAL__latency_qpl_marker_id":36707139,"INTERNAL__latency_qpl_instance_id":102159124600186,"is_bloks":1,"tag_source":"tag_selection_screen"}}',
                                '_uuid': '3ae08b3b-5663-48eb-88af-30364bc3201e',
                                'bk_client_context':
                                    '{"bloks_version":"0ee04a4a6556c5bb584487d649442209a3ae880ae5c6380b16235b870fcc4052","styles_id":"instagram"}',
                                'bloks_versioning_id':
                                    '0ee04a4a6556c5bb584487d649442209a3ae880ae5c6380b16235b870fcc4052',
                            }
                            req = requests.post('https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.instagram_bloks_bottom_sheet.ixt.screen.frx_tag_selection_screen/',data=data,headers=headers)
                            context = re.search(r'\"tag_selection_screen\", \"(.*?)\", ',str(req.json())).group(1)
                            data = {
                                'params':
                                    '{"client_input_params":{"tags":["ig_nudity_or_pornography_v3","ig_nudity_v2"]},"server_params":{"show_tag_search":1,"serialized_state":"'+context+'","INTERNAL__latency_qpl_marker_id":36707139,"INTERNAL__latency_qpl_instance_id":102164812700034,"is_bloks":1,"tag_source":"tag_selection_screen"}}',
                                '_uuid': '3ae08b3b-5663-48eb-88af-30364bc3201e',
                                'bk_client_context':
                                    '{"bloks_version":"0ee04a4a6556c5bb584487d649442209a3ae880ae5c6380b16235b870fcc4052","styles_id":"instagram"}',
                                'bloks_versioning_id':
                                    '0ee04a4a6556c5bb584487d649442209a3ae880ae5c6380b16235b870fcc4052',
                            }
                            req = requests.post('https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.instagram_bloks_bottom_sheet.ixt.screen.frx_tag_selection_screen/',data=data,headers=headers)
                            context = re.search(r'\(bk.action.array.Make, \(bk.action.i32.Const, -1\), \"(.*?)\", ',str(req.json())).group(1)
                            data = {
                                'params':
                                    '{"server_params":{"channel":-1,"serialized_state":"'+context+'","INTERNAL__latency_qpl_marker_id":36707139,"INTERNAL__latency_qpl_instance_id":102636218000006}}',
                                '_uuid': '3ae08b3b-5663-48eb-88af-30364bc3201e',
                                'bk_client_context':
                                    '{"bloks_version":"0ee04a4a6556c5bb584487d649442209a3ae880ae5c6380b16235b870fcc4052","styles_id":"instagram"}',
                                'bloks_versioning_id':
                                    '0ee04a4a6556c5bb584487d649442209a3ae880ae5c6380b16235b870fcc4052',
                            }
                            req = requests.post('https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.instagram_bloks_bottom_sheet.ixt.screen.frx_report_review_screen/',data=data,headers=headers)
                            context = re.search(r' \"serialized_state\", \"INTERNAL__latency_qpl_marker_id\", \"INTERNAL__latency_qpl_instance_id\"\), \(bk.action.array.Make, \"(.*?)\", ',str(req.json())).group(1)
                            data = {
                                'params':
                                    '{"server_params":{"serialized_state":"'+context+'","INTERNAL__latency_qpl_marker_id":36707139,"INTERNAL__latency_qpl_instance_id":103086232600005}}',
                                '_uuid': '3ae08b3b-5663-48eb-88af-30364bc3201e',
                                'bk_client_context':
                                    '{"bloks_version":"0ee04a4a6556c5bb584487d649442209a3ae880ae5c6380b16235b870fcc4052","styles_id":"instagram"}',
                                'bloks_versioning_id':
                                    '0ee04a4a6556c5bb584487d649442209a3ae880ae5c6380b16235b870fcc4052',
                            }
                            req = requests.post('https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.instagram_bloks_bottom_sheet.ixt.screen.frx_post_report_process_timeline/',data=data,headers=headers)
                            if req.text.__contains__('"status":"ok"'):
                                self.done += 1
                            else:
                                self.error += 1
                        
                        elif self.report_type == 6:
                            data = {
                                'params':
                                    '{"client_input_params":{"tags":["ig_bullying_or_harassment_comment_v3"]},"server_params":{"show_tag_search":1,"serialized_state":"'+context+'","INTERNAL__latency_qpl_marker_id":36707139,"INTERNAL__latency_qpl_instance_id":104140233500262,"is_bloks":1,"tag_source":"tag_selection_screen"}}',
                                '_uuid': '3ae08b3b-5663-48eb-88af-30364bc3201e',
                                'bk_client_context':
                                    '{"bloks_version":"0ee04a4a6556c5bb584487d649442209a3ae880ae5c6380b16235b870fcc4052","styles_id":"instagram"}',
                                'bloks_versioning_id':
                                    '0ee04a4a6556c5bb584487d649442209a3ae880ae5c6380b16235b870fcc4052',
                            }
                            req = requests.post('https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.instagram_bloks_bottom_sheet.ixt.screen.frx_tag_selection_screen/',data=data,headers=headers)
                            context = re.search(r'\"tag_selection_screen\", \"(.*?)\", ',str(req.json())).group(1)
                            data = {
                                'params':
                                    '{"client_input_params":{"tags":["ig_bullying_or_harassment_me_v3","ig_bullying_or_harassment_comment_v3"]},"server_params":{"show_tag_search":1,"serialized_state":"'+context+'","INTERNAL__latency_qpl_marker_id":36707139,"INTERNAL__latency_qpl_instance_id":104413924200047,"is_bloks":1,"tag_source":"tag_selection_screen"}}',
                                '_uuid': '3ae08b3b-5663-48eb-88af-30364bc3201e',
                                'bk_client_context':
                                    '{"bloks_version":"0ee04a4a6556c5bb584487d649442209a3ae880ae5c6380b16235b870fcc4052","styles_id":"instagram"}',
                                'bloks_versioning_id':
                                    '0ee04a4a6556c5bb584487d649442209a3ae880ae5c6380b16235b870fcc4052',
                            }
                            req = requests.post('https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.instagram_bloks_bottom_sheet.ixt.screen.frx_tag_selection_screen/',data=data,headers=headers)
                            context = re.search(r' \"report\", \"(.*?)\", ',str(req.json())).group(1)
                            data = {
                                'params':
                                    '{"server_params":{"serialized_state":"'+context+'","INTERNAL__latency_qpl_marker_id":36707139,"INTERNAL__latency_qpl_instance_id":104693808800002,"selected_option":"report"}}',
                                '_uuid': '3ae08b3b-5663-48eb-88af-30364bc3201e',
                                'bk_client_context':
                                    '{"bloks_version":"0ee04a4a6556c5bb584487d649442209a3ae880ae5c6380b16235b870fcc4052","styles_id":"instagram"}',
                                'bloks_versioning_id':
                                    '0ee04a4a6556c5bb584487d649442209a3ae880ae5c6380b16235b870fcc4052',
                            }
                            req = requests.post('https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.instagram_bloks_bottom_sheet.ixt.screen.frx_policy_education/',data=data,headers=headers)
                            context = re.search(r', \"serialized_state\", \"INTERNAL__latency_qpl_marker_id\", \"INTERNAL__latency_qpl_instance_id\"\), \(bk.action.array.Make, \"(.*?)\",',str(req.json())).group(1)
                            data = {
                                'params':
                                    '{"server_params":{"serialized_state":"'+context+'","INTERNAL__latency_qpl_marker_id":36707139,"INTERNAL__latency_qpl_instance_id":105124220100005}}',
                                '_uuid': '3ae08b3b-5663-48eb-88af-30364bc3201e',
                                'bk_client_context':
                                    '{"bloks_version":"0ee04a4a6556c5bb584487d649442209a3ae880ae5c6380b16235b870fcc4052","styles_id":"instagram"}',
                                'bloks_versioning_id':
                                    '0ee04a4a6556c5bb584487d649442209a3ae880ae5c6380b16235b870fcc4052',
                            }
                            req = requests.post('https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.instagram_bloks_bottom_sheet.ixt.screen.frx_post_report_process_timeline/',data=data,headers=headers)
                            if req.text.__contains__('"status":"ok"'):
                                self.done += 1
                            else:
                                self.error += 1
                        elif self.report_type == 7:
                            data = {
                                'params':
                                    '{"client_input_params":{"tags":["ig_bullying_or_harassment_comment_v3"]},"server_params":{"show_tag_search":1,"serialized_state":"'+context+'","INTERNAL__latency_qpl_marker_id":36707139,"INTERNAL__latency_qpl_instance_id":104140233500262,"is_bloks":1,"tag_source":"tag_selection_screen"}}',
                                '_uuid': '3ae08b3b-5663-48eb-88af-30364bc3201e',
                                'bk_client_context':
                                    '{"bloks_version":"0ee04a4a6556c5bb584487d649442209a3ae880ae5c6380b16235b870fcc4052","styles_id":"instagram"}',
                                'bloks_versioning_id':
                                    '0ee04a4a6556c5bb584487d649442209a3ae880ae5c6380b16235b870fcc4052',
                            }
                            req = requests.post('https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.instagram_bloks_bottom_sheet.ixt.screen.frx_tag_selection_screen/',data=data,headers=headers)
                            context = re.search(r'\"tag_selection_screen\", \"(.*?)\", ',str(req.json())).group(1)
                            data = {
                                'params':
                                    '{"client_input_params":{"tags":["ig_bullying_or_harassment_me_v3","ig_bullying_or_harassment_comment_v3"]},"server_params":{"show_tag_search":1,"serialized_state":"'+context+'","INTERNAL__latency_qpl_marker_id":36707139,"INTERNAL__latency_qpl_instance_id":104413924200047,"is_bloks":1,"tag_source":"tag_selection_screen"}}',
                                '_uuid': '3ae08b3b-5663-48eb-88af-30364bc3201e',
                                'bk_client_context':
                                    '{"bloks_version":"0ee04a4a6556c5bb584487d649442209a3ae880ae5c6380b16235b870fcc4052","styles_id":"instagram"}',
                                'bloks_versioning_id':
                                    '0ee04a4a6556c5bb584487d649442209a3ae880ae5c6380b16235b870fcc4052',
                            }
                            req = requests.post('https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.instagram_bloks_bottom_sheet.ixt.screen.frx_tag_selection_screen/',data=data,headers=headers)
                            context = re.search(r' \"report\", \"(.*?)\", ',str(req.json())).group(1)
                            data = {
                                'params':
                                    '{"server_params":{"serialized_state":"'+context+'","INTERNAL__latency_qpl_marker_id":36707139,"INTERNAL__latency_qpl_instance_id":104693808800002,"selected_option":"report"}}',
                                '_uuid': '3ae08b3b-5663-48eb-88af-30364bc3201e',
                                'bk_client_context':
                                    '{"bloks_version":"0ee04a4a6556c5bb584487d649442209a3ae880ae5c6380b16235b870fcc4052","styles_id":"instagram"}',
                                'bloks_versioning_id':
                                    '0ee04a4a6556c5bb584487d649442209a3ae880ae5c6380b16235b870fcc4052',
                            }
                            req = requests.post('https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.instagram_bloks_bottom_sheet.ixt.screen.frx_policy_education/',data=data,headers=headers)
                            context = re.search(r', \"serialized_state\", \"INTERNAL__latency_qpl_marker_id\", \"INTERNAL__latency_qpl_instance_id\"\), \(bk.action.array.Make, \"(.*?)\",',str(req.json())).group(1)
                            data = {
                                'params':
                                    '{"server_params":{"serialized_state":"'+context+'","INTERNAL__latency_qpl_marker_id":36707139,"INTERNAL__latency_qpl_instance_id":105124220100005}}',
                                '_uuid': '3ae08b3b-5663-48eb-88af-30364bc3201e',
                                'bk_client_context':
                                    '{"bloks_version":"0ee04a4a6556c5bb584487d649442209a3ae880ae5c6380b16235b870fcc4052","styles_id":"instagram"}',
                                'bloks_versioning_id':
                                    '0ee04a4a6556c5bb584487d649442209a3ae880ae5c6380b16235b870fcc4052',
                            }
                            req = requests.post('https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.instagram_bloks_bottom_sheet.ixt.screen.frx_post_report_process_timeline/',data=data,headers=headers)
                            if req.text.__contains__('"status":"ok"'):
                                self.done += 1
                            else:
                                self.error += 1
                    except:
                        self.error += 1
                    print(f" {Fore.LIGHTCYAN_EX}[ {Fore.LIGHTWHITE_EX}Done : {Fore.LIGHTGREEN_EX}{self.done} {Fore.LIGHTWHITE_EX}, {Fore.LIGHTWHITE_EX}Errors : {Fore.RED}{self.error} {Fore.LIGHTCYAN_EX}]", end='\r')
                    
                    time.sleep(self.sleep)

if __name__=="__main__":
    Report()
