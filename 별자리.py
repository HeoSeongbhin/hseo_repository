Star_Sign_data = {
	"물병자리":  ("01-20", "02-18"),
	"물고기자리": ("02-19", "03-20"),
	"양자리": ("03-21", "04-19"),
	"황소자리": ("04-20", "05-20"), 
	"쌍둥이자리": ("05-21", "06-28"),
	"게자리": ("06-21", "07-22"),
	"사자자리": ("07-23", "08-22"),
	"처녀자리": ("08-23", "09-22"),
	"천칭자리": ("09-23", "10-22"),
	"전갈자리": ("10-23", "11-21"),
	"사수자리": ("11-22", "12-21"),
	"염소자리": ("12-22", "01-19"),
}

st=input ("생년월일:")
ar=st.split("-")
# print (ar)
year=int(ar[0])
month=ar[1] 
day=ar[2]
md=int(month+day)
#print(md)
n=0

def feb():
	if year%4==0 and year%100!=0 or year%400==0:
		if md>=219 and md<=229:
			print("당신의 별자리는 물고기자리 입니다.")
		elif md==230 or md==231:
			print("유효하지 않은 날짜 형식입니다.")
	elif year%4!=0 and year%400!=0:
		if md>=219 and md<=228:
			print("당신의 별자리는 물고기자리 입니다.")
		elif md==229 or md==230 or md==231:
			print("유효하지 않은 날짜 형식입니다.")
			
for i,(j,k) in Star_Sign_data.items():
	ft=j.split("-")
	tt=k.split("-")
	if md<=219 or md>=231:
		if md>=int(ft[0]+ft[1]) and md<=int(tt[0]+tt[1]):
			if int(day)>=1 and int(day)<=31:
				print("당신의 별자리는",i,"입니다.")
				n=1	
if md>=220 and md<=230:
	feb()
	n=1
elif md>=1222 and md<=1231:
	print("당신의 별자리는",i,"입니다.")
	n=1
elif md>=101 and md<=119:
	print("당신의 별자리는",i,"입니다.")
	n=1
	
elif n==0:
	print("유효하지 않은 날짜 형식입니다.")

