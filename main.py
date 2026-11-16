import os,json,urllib.request as U
D={2:(31,33,14,18,-31,-33,-14,-18),3:(15,17,-15,-17),4:(1,16,-1,-16)}
D[5]=D[6]=D[3]+D[4]
V=0,100,320,335,500,950,20000
S=[i for i in range(128) if not i&136]
R={0:2,4:3,7:1,112:8,116:12,119:4}
E={}
C={i:7-abs(2*(i%16)-7)-abs(2*(i//16)-7) for i in S}
for p in range(-6,7):
 for i in S:
  a=abs(p);r=i//16 if p>0 else 7-i//16;c=C[i]
  E[p,i]=(2*(p>0)-1)*(V[a]+(r*8+c*2 if a==1 else c*5 if a in (2,3) else r*2 if a==4 else -c*3 if a==6 else c)) if p else 0
def fen(f):
 a,t,c,e,h,*_=f.split();b=[0]*128;i=112
 for x in a:
  if x=='/':i-=24
  elif x.isdigit():i+=int(x)
  else:b[i]=' PNBRQK'.index(x.upper())*(1 if x.isupper() else -1);i+=1
 return tuple(b),1 if t=='w' else -1,sum(1<<'KQkq'.find(x) for x in c if x!='-'),-1 if e=='-' else ord(e[0])-97+16*(int(e[1])-1),int(h),sum(E[b[i],i] for i in S)
def att(b,k,t):
 for d in D[6]+D[2]:
  j=k+d;n=1
  while not j&136:
   p=b[j]*t
   if p:
    if p>0 and (p==5 and d in D[6] or p==4 and d in D[4] or p==3 and d in D[3] or n==1 and (p==6 and d in D[6] or p==2 and d in D[2] or p==1 and d in (-16*t-1,-16*t+1))):return 1
    break
   if d in D[2]:break
   j+=d;n+=1
 return 0
def ck(b,t):return att(b,b.index(6*t),-t)
def do(s,m):
 o,t,c,e,h,v=s;i,j,p=m;b=list(o);q=b[i];n=[i,j];b[i]=0;b[j]=p or q
 if abs(q)==1 and j==e:n+=[j-16*t];b[n[-1]]=0
 if abs(q)==6 and abs(j-i)==2:
  r=i+3 if j>i else i-4;k=(i+j)//2;n+=[r,k];b[k]=b[r];b[r]=0
 return tuple(b),-t,c&~(R.get(i,0)|R.get(j,0)),(i+j)//2 if abs(q)==1 and abs(j-i)==32 else -1,0 if o[j] or abs(q)==1 else h+1,v+sum(E[b[k],k]-E[o[k],k] for k in n)
def gen(s):
 b,t,c,e,h,v=s
 for i in S:
  v=b[i]*t
  if v<1:continue
  A=[]
  if v==1:
   j=i+16*t
   if not j&136 and not b[j]:
    A.append(j);k=j+16*t
    if i//16==(1 if t==1 else 6) and not b[k]:A.append(k)
   for j in (i+15*t,i+17*t):
    if not j&136 and (b[j]*t<0 or j==e):A.append(j)
  else:
   for d in D[v]:
    j=i+d
    while not j&136:
     if b[j]*t>0:break
     A.append(j)
     if b[j] or v in (2,6):break
     j+=d
   if v==6 and i==(4 if t==1 else 116) and not ck(b,t):
    for f,d,r in ((1 if t==1 else 4,1,i+3),(2 if t==1 else 8,-1,i-4)):
     if f&c and b[r]==4*t and all(not b[k] for k in range(min(i,r)+1,max(i,r))) and not att(b,i+d,-t):A.append(i+2*d)
  for j in A:
   for p in ((2*t,3*t,4*t,5*t) if v==1 and j//16 in (0,7) else (0,)):yield i,j,p
def uci(m):
 i,j,p=m
 return ''.join(chr(97+k%16)+str(1+k//16) for k in (i,j))+(' pnbrqk'[abs(p)] if p else '')
def neg(s,d,a,b,l=0,P=()):
 global N
 N+=1
 if N>32000:raise StopIteration
 B,t,c,e,h,g=s;o=T.get(s);a0=a;ch=ck(B,t)
 if o and o[0]>=d>0 and s[:4] not in P:
  _,w,f,m=o;w-=l*(2*(w>0)-1) if abs(w)>29000 else 0
  if f==0 or f==1 and w>=b or f==-1 and w<=a:return w
 A=list(gen(s));v=-31000;M=None;n=0;q=d<=0 and not ch
 v0=(g+25*((B.count(3)>1)-(B.count(-3)>1)))*t
 if not(5 in B or -5 in B):v0+=8*(C[B.index(6)]-C[B.index(-6)])*t
 if q:v=v0
 A.sort(key=lambda m:(m==(o[3] if o else None),10*V[abs(B[m[1]])]-V[abs(B[m[0]])]+V[abs(m[2])] if B[m[1]] or m[2] else H.get(m,0)/100),reverse=1)
 for m in A:
  z=do(s,m)
  if ck(z[0],t):continue
  n+=1
  if h>=100 or s[:4] in P:return 0
  if d<-6:return v0
  if q:
   if v>=b:return v
   a=max(a,v)
   if not(B[m[1]] or m[2] or abs(B[m[0]])==1 and m[1]==e):continue
  w=-neg(z,d-1,-b,-a,l+1,P+(s[:4],))
  if w>v:v=w;M=m
  a=max(a,w)
  if a>=b:H[m]=H.get(m,0)+max(d,0)**2;break
 if not n:return -30000+l if ch else 0
 if d>0:T[s]=d,v+(l*(2*(v>0)-1) if abs(v)>29000 else 0),1 if v>=b else -1 if v<=a0 else 0,M
 return v
def pick(s,L):
 global N,T,H
 N=0;T={};H={};r=[m for m in gen(s) if uci(m) in L];u=r[0]
 for d in range(1,9):
  try:
   neg(s,d,-31000,31000);m=T[s][3]
   if m in r:u=m
  except StopIteration:break
 return uci(u)
if __name__=='__main__':
 def api(p,x):
  return json.load(U.urlopen(U.Request(os.environ['MAKEFUN_ENV_URL']+p,json.dumps(x).encode(),{'Content-Type':'application/json'}),timeout=180))
 g=api('/game',{})
 while g['status']!='done':
  g=api('/game',{}) if g['status']=='over' else api('/move',dict(game=g['game'],move=pick(fen(g['fen']),g['legal_moves'])))
