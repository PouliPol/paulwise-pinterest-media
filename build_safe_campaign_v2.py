#!/usr/bin/env python3
"""Original vector editorial scene/mockup generator; NOT actual product photos."""
from pathlib import Path
from html import escape
import json, math, random, subprocess
ROOT=Path("/home/master/gse/paulwise-pinterest-media")
OUT=ROOT/"pins"/"home-safes-v2-2026-11-09"
OUT.mkdir(parents=True,exist_ok=True)
PRODUCTS=[
("amazon-basics","Amazon Basics Electronic Security Safe","basic","cabinet","A drawer is not a security plan","Know what needs protecting","Small space. Smarter storage.","The mounting detail matters","Give everyday valuables a home"),
("sentrysafe-1160","SentrySafe 1160 Fire Chest","basic","chest","Would your documents survive?","Protect the irreplaceable papers","Fire protection is not burglary protection","Check the rating, not the label","Keep records ready when it matters"),
("kavey-digital","Kavey Digital Home Safe","basic","cabinet","What is in your unlocked drawer?","Your essentials deserve a place","A keypad is only the beginning","Look beyond the lock","A daily habit of secure storage"),
("executivesafe-acs4","ExecutiveSafe ACS-4 Laptop Safe","basic","laptop","A laptop is more than a device","Keep work and records together","Measure before you buy","Think about anchoring first","Protect your workday essentials"),
("pockrif-large","Pockrif 19.69-inch Large Safe","basic","tall","More space. Still needs security.","Organize the things you value","Do not confuse size with strength","Installation changes the result","Compare capacity, not just price"),
("topmeda-biometric","TOPMEDA Biometric Lockbox","portable","fingerprint","Private access starts with a plan","A bedside drawer is not a lock","Speed needs reliability","Backup access matters","Review real-world storage needs"),
("vehicle-biometric","Biometric Vehicle Lockbox","portable","vehicle","A car is not secure storage","Portable does not mean protected","Think beyond the lockbox","Secure placement is essential","Know the transport rules"),
("smart-wifi","Smart WiFi Bedside Safe","portable","smart","Convenience is not certification","A smarter bedside routine","Check how backup access works","Your privacy is worth a plan","Technology is only one layer"),
("ctsafepro","CTSAFEPRO Biometric Lockbox","portable","compact","Keep private items secured","Check the locking mechanism","A compact box needs a plan","Test the backup access","Compare before you trust a claim"),
("fingerprint-portable","Portable Fingerprint Lockbox","portable","travel","What travels with your valuables?","Small boxes have big limitations","Your documents need a system","A lockbox is not an anchor","Make a better travel checklist"),
("premium-82","8.2 cu. ft. Biometric Home Safe","premium","vault","Quiet luxury is deliberate","A collection deserves thoughtful care","Big does not mean certified","Elegant design. Verified security?","Buy evidence, not expensive hype"),
]
SCENES=[
("The morning routine","warm residential interior, sideboard and quiet daylight"),
("A private place","bright contemporary office with shelves"),
("The close inspection","minimal stone-and-steel studio"),
("An organized household","rich walnut residence at dusk"),
("A considered choice","premium editorial setting with directional light"),
]
PAL=[
("#263b3f","#cfa376","#0f1b20","#8bbeb6"),
("#2f3841","#b6a08b","#141e27","#77c5d0"),
("#393133","#c99d74","#1f1d1e","#d6aa7a"),
("#3d332c","#d3a67f","#211d1a","#b9b9ac"),
("#232a29","#c8ab78","#0c1517","#b4a174")
]
FONT="DejaVu Sans"
def rect(x,y,w,h,fill,rx=0,extra=""):return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" {extra}/>'
def line(x1,y1,x2,y2,color,sw=2,extra=""):return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{sw}" {extra}/>'
def tx(x,y,v,sz=30,color="#fff",wt="normal",a="start",spacing="0"):return f'<text x="{x}" y="{y}" font-family="{FONT}" font-size="{sz}" font-weight="{wt}" letter-spacing="{spacing}" fill="{color}" text-anchor="{a}">{escape(v)}</text>'
def circle(x,y,r,fill,other=""):return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}" {other}/>'
def plant(x,y,s=1):
 out=[f'<g transform="translate({x} {y}) scale({s})">']
 out+=[rect(-44,8,90,82,"#8b7260",7),rect(-51,6,103,11,"#c6ab85",6)]
 for a in [-80,-47,-20,17,38,70]:
  out.append(line(0,7,a,-125+abs(a)*.13,"#586d55",5))
  out.append(f'<ellipse cx="{a}" cy="{-108+abs(a)*.13}" rx="22" ry="51" fill="{["#6c885f","#415a43","#55764d"][abs(a)%3]}" transform="rotate({a*.2} {a} {-108+abs(a)*.13})"/>')
 out.append("</g>");return "".join(out)
def prop(name,variation,px,py):
 if name=="premium":
  return "".join([rect(px,py,180,52,"#583d30",6),rect(px+8,py-45,165,48,"#452c22",5),circle(px+63,py-17,23,"#dabf8a"),circle(px+122,py-17,23,"#b4a487"),tx(px,py+94,"PRIVATE COLLECTION",18,"#dbc49f","bold")])
 if name=="portable":
  if variation%2:
   return "".join([rect(px,py,180,19,"#3b403e",4),rect(px+11,py-99,151,103,"#232c31",9),rect(px+17,py-94,137,87,"#77969a",7),rect(px+26,py-81,117,66,"#18303c",5),tx(px+83,py-43,"ACCESS",14,"#badad6","bold","middle")])
  return "".join([rect(px,py,135,85,"#4e443b",5),rect(px+14,py+6,104,71,"#baa590",4),line(px+27,py+34,px+106,py+34,"#756151",3),line(px+27,py+48,px+108,py+48,"#756151",3)])
 return "".join([rect(px,py,172,106,"#57463a",5),rect(px+15,py-9,165,104,"#b8a182",5),rect(px+20,py-2,150,83,"#e7d5b2",3),line(px+28,py+31,px+143,py+31,"#998367",3),line(px+28,py+48,px+121,py+48,"#998367",3)])
def room(pid,day,seg,pal):
 base,wood,dark,acc=pal
 r=[]
 r.append(rect(0,0,1000,1500,f"url(#bg{day})"))
 r.append(rect(0,345,1000,720,f"url(#wall{day})"))
 if day==0:
  r+=[rect(710,362,220,460,"#b2c9bf",8),rect(723,374,192,430,"#89a6a7",4),rect(748,376,16,427,"#ece0c5"),line(832,373,832,803,"#ede2d1",11),line(718,584,917,584,"#ede2d1",9)]
  r.append(plant(115,826,1.12))
 elif day==1:
  r+=[rect(34,440,288,532,"#304047",4)]
  for j in range(4):r+=[rect(43,507+j*96,266,11,"#93785d",2),rect(61+j*33,438+j*100+24,80,69,"#67634e",3)]
  r.append(plant(875,832,.92))
 elif day==2:
  r+=[rect(20,384,956,572,"#303332",2)]
  for j in range(9):r.append(line(32,402+j*68,973,402+j*68,"#555859",1))
  r+=[circle(817,559,106,"#927b58", 'opacity=".21"'),rect(780,484,72,175,"#574b3b",8)]
 elif day==3:
  for j in range(10):r.append(rect(40+j*110,350,14,614,"#4c3d32",2))
  r+=[rect(73,448,208,13,"#b38c6a"),rect(73,625,208,13,"#b38c6a"),circle(189,579,46,"#b68b61", 'opacity=".45"')]
  r.append(plant(856,795,.82))
 else:
  r+=[rect(16,348,960,625,"#1c2829",4),rect(42,372,911,585,"#303d3c",1)]
  for j in range(7):r.append(line(70+j*140,370,70+j*140,950,"#5b6b60",2))
  r.append(plant(118,814,.8))
 r.append('<path d="M0 912 L1000 912 L1000 1162 L0 1162Z" fill="url(#desk)" />')
 r.append(rect(0,909,1000,28,"#c5a783",2))
 r.append(prop(seg,day,720 if pid%3==0 else 86,940))
 return "".join(r)
def render_safe(kind,day,seg):
 c="#151b20" if seg!="premium" else "#22272b"; face="#263138"
 if kind in ("vault","tall"):
  x=295 if kind=="vault" else 350;y=449 if kind=="vault" else 515
  w=467 if kind=="vault" else 380;h=585 if kind=="vault" else 515
  obj=f'<g filter="url(#shad)">{rect(x-28,y-12,w+36,h+28,"#11191d",12)}'
  obj+=f'<path d="M{x+5} {y+9} l44 -29 h{w-37} l-41 29Z" fill="#596063"/>'
  obj+=rect(x,y,w,h,"url(#steel)",12, 'stroke="#69777a" stroke-width="6"')
  obj+=rect(x+24,y+24,w-53,h-52,"url(#face)",7,'stroke="#11181a" stroke-width="9"')
  obj+=rect(x+w-24,y+62,18,76,"#9ca7aa",5)+rect(x+w-24,y+h-121,18,76,"#9ca7aa",5)
  obj+=rect(x+55,y+156,85,129,"#131e23",12,'stroke="#8f9ea1" stroke-width="4"')
  obj+=circle(x+97,y+190,23,"#617f84", 'stroke="#b5c9c9" stroke-width="2"')+tx(x+97,y+198,"●",22,"#a9d8d8","bold","middle")
  for row in range(3):
   for col in range(3):obj+=circle(x+70+col*27,y+240+row*18,5,"#8aacae")
  obj+=rect(x+139,y+307,137,15,"#abb5b7",6)+circle(x+145,y+311,24,"#bbc2c2")
  obj+="</g>";return obj
 # all smaller model types, show medium/box style
 wide = kind in ("chest","laptop","smart","vehicle","travel","compact","fingerprint")
 w=560 if wide else 460;h=290 if wide else 420
 x=(1000-w)//2+18;y=618 if wide else 548
 if kind=="vehicle":y=652
 if kind=="travel":y=652
 if kind=="chest":y=657
 obj='<g filter="url(#shad)">'
 obj+=f'<path d="M{x-31} {y+23} L{x+9} {y-27} H{x+w+34} L{x+w} {y+26}Z" fill="#626b6f"/>'
 obj+=rect(x-25,y+12,w+61,h+31,"#151c1d",16)
 obj+=rect(x,y,w,h,"url(#steel)",17,'stroke="#657076" stroke-width="5"')
 obj+=rect(x+21,y+22,w-44,h-44,"url(#face)",10, 'stroke="#121a1f" stroke-width="9"')
 if kind=="chest":
  obj+=rect(x+19,y-62,w-38,105,"#151b1d",14,'stroke="#707a79" stroke-width="6"')
  obj+=rect(x+52,y-41,w-105,68,"#c5ba9e",4)
  obj+=rect(x+66,y-29,w-130,12,"#dbcdab",2)
  obj+=rect(x+w*.39,y+h*.49,126,65,"#1d2426",12,'stroke="#989e98" stroke-width="4"')
 elif kind in ("fingerprint","smart","compact","vehicle","travel"):
  if kind=="travel":obj+=rect(x+w*.39,y-38,w*.22,48,"#181e1f",11,'stroke="#889195" stroke-width="8"')
  obj+=rect(x+w*.37,y+70,148,92,"#111a1d",12,'stroke="#76919a" stroke-width="4"')
  obj+=circle(x+w*.37+73,y+105,29,"#2f7c88",'stroke="#8fc5ce" stroke-width="4"')
  obj+=tx(x+w*.37+73,y+114,"◌",28,"#adf0ed","bold","middle")
 else:
  obj+=rect(x+w*.34,y+93,148,120,"#141c20",12,'stroke="#9aa6a5" stroke-width="3"')
  obj+=circle(x+w*.34+36,y+132,20,"#9caaa9")
  for row in range(3):
   for col in range(3):obj+=circle(x+w*.34+81+col*17,y+117+row*22,5,"#bdc5c5")
  obj+=rect(x+w*.34+11,y+181,30,6,"#aebabb",4)
 if kind=="laptop":obj+=rect(x+110,y+251,304,19,"#788483",4)
 obj+="</g>"
 return obj
def headline_lines(s,maxlen=22):
 parts=s.upper().split();lines=[];cur=""
 for p in parts:
  if cur and len(cur)+1+len(p)>maxlen:lines.append(cur);cur=p
  else:cur=(cur+" "+p).strip()
 if cur:lines.append(cur)
 return lines[:3]
def svg(p,day):
 slug,name,seg,kind,*hooks=p;hook=hooks[day]; base,wood,dark,accent=PAL[day]
 top="#1a272a" if seg!="premium" else "#2a2926"
 cta={"basic":"#f2b88d","portable":"#9ed5d0","premium":"#e8c997"}[seg]
 label={"basic":"ESSENTIAL / EVERYDAY STORAGE","portable":"PORTABLE / CONTROLLED ACCESS","premium":"PREMIUM / PRIVATE COLLECTION"}[seg]
 r=['<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="1500" viewBox="0 0 1000 1500">']
 r.append(f"""<defs>
  <linearGradient id="bg{day}" x1="0" y1="0" x2="1" y2="1"><stop stop-color="{top}"/><stop offset="1" stop-color="#10191c"/></linearGradient>
  <linearGradient id="wall{day}" x1="0" y1="0" x2="1" y2="1"><stop stop-color="{wood}"/><stop offset=".46" stop-color="{base}"/><stop offset="1" stop-color="{dark}"/></linearGradient>
  <linearGradient id="steel" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#747f81"/><stop offset=".16" stop-color="#344146"/><stop offset=".72" stop-color="#181f23"/><stop offset="1" stop-color="#070d11"/></linearGradient>
  <linearGradient id="face" x1="0" y1="0" x2=".9" y2="1"><stop stop-color="#39464b"/><stop offset=".7" stop-color="#242e34"/><stop offset="1" stop-color="#121a20"/></linearGradient>
  <linearGradient id="desk" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#644b3d"/><stop offset=".53" stop-color="#957358"/><stop offset="1" stop-color="#2d2926"/></linearGradient>
  <filter id="shad" x="-30%" y="-30%" width="160%" height="170%"><feGaussianBlur in="SourceAlpha" stdDeviation="14"/><feOffset dy="16"/><feComponentTransfer><feFuncA type="linear" slope=".62"/></feComponentTransfer><feMerge><feMergeNode/><feMergeNode in="SourceGraphic"/></feMerge></filter>
  </defs>""")
 r.append(room(PRODUCTS.index(p),day,seg,PAL[day]))
 r.append(render_safe(kind,day,seg))
 r.append(rect(0,0,1000,385,"#0c171a",0,'opacity=".91"'))
 r.append(rect(60,55,74,7,cta,3))
 r.append(tx(150,69,"PAULWISE.ONLINE",28,"#f1f4ee","bold",spacing="2"))
 r.append(tx(62,139,label,24,cta,"bold",spacing="1.2"))
 lines=headline_lines(hook,19)
 for i,l in enumerate(lines):r.append(tx(60,216+i*63,l,51,"#fff","bold"))
 # gradient overlay not supported as opacity? lower solid dark
 r.append(rect(0,1137,1000,363,"#081418"))
 r.append(rect(55,1163,890,264,"#121d22",24, 'stroke="'+cta+'" stroke-width="3"'))
 r.append(tx(90,1217,"FEATURED IN THE BUYER'S GUIDE",21,cta,"bold",spacing=".7"))
 names=[name]
 if len(name)>39:
  words=name.split();names=[];s=""
  for w in words:
   if len(s)+len(w)+1>39:names.append(s);s=w
   else:s=(s+" "+w).strip()
  if s:names.append(s)
 for i,v in enumerate(names[:2]):r.append(tx(90,1274+i*42,v,31,"#f4f4ef","bold"))
 r.append(rect(90,1359,820,54,cta,13))
 r.append(tx(500,1396,"SEE THE BUYING GUIDE",24,"#10191d","bold","middle"))
 r.append(tx(66,1464,"EDITORIAL ILLUSTRATION • NOT AN EXACT MODEL PHOTO • AFFILIATE GUIDE",16,"#b2bbb8"))
 r.append("</svg>")
 return "\n".join(r)
manifest=[]
for i,p in enumerate(PRODUCTS):
 for day in range(5):
  slug=p[0];file=f"{slug}_day{day+1}.jpg";src=OUT/(file+'.svg')
  src.write_text(svg(p,day),encoding="utf8")
  manifest.append(dict(slug=slug,model=p[1],segment=p[2],day=day+1,headline=p[4+day],file=file,source=str(src)))
(OUT/"manifest.json").write_text(json.dumps(manifest,indent=2),encoding="utf8")
print("SVG_CREATED",len(manifest))
