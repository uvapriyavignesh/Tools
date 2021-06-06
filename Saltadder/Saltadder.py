import os
import sys
import argparse
import threading
pasr=argparse.ArgumentParser(description="Salt Adder in PasswordList",epilog='''Usage Instruction :
                                                                                                       ./saltadder -s salt -p passwordlist -t threads -l 0 -o OutputFile ''')
pasr.add_argument("-s",dest="Salt",help="Specify Salt",required=True,type=str)
pasr.add_argument("-p",dest="password",help="Specify passwordList Location",required=True)
pasr.add_argument("-l",dest="place",help="Specify Salt adding Place front=0,back=1,both=2",required=True,type=int)
pasr.add_argument("-t",dest="Threads",help="Specify Threads to run",type=int)
pasr.add_argument("-o",dest="Output",help="Specify Output file name",required=True)
args =pasr.parse_args()
print (args)
try:
  os.path.exists(args.password)
  f=open(args.password,"r").readlines()
except Exception as e:
 
  sys.exit("[*]Your password file is not Found")

sa=args.Salt
name=args.place
rg=args.Threads
def addpo(na):
  if os.path.exists(args.Output):
      f1=open (args.Output,"a")
      if (name==0):
              out= sa+na
              f1.write(out+"\n")
              f1.close()
      elif (name==1):
                out= na+sa
                f1.write(out+"\n")
                f1.close()
      elif (name==2):
               out= sa+na+sa
               f1.write(out+"\n")
               f1.close()
  else:
      f = open(args.Output, "x")
      f.close()
      f1=open (args.Output,"a")
      if (name==0):
              out= sa+na
              f1.write(out+"\n")
              f1.close()
      elif (name==1):
                out= na+sa
                f1.write(out+"\n")
                f1.close()
      elif (name==2):
               out= sa+na+sa
               f1.write(out+"\n")
               f1.close()           

def notrd():
    for sd in f:
        sd=sd.rstrip()
        addpo(sd)
def thread(count):
    if ( count==0):
        for ad in range(0,rg) :
             sb=f[ad]
             ss=sb.rstrip()
             addpo(ss)
    else:
        end=count*rg
        st=end-(rg-1)
        for ad in range(st,end) :
             sb=f[ad]
             ss=sb.rstrip()
             addpo(ss)
if (rg==None):
     notrd()

else:
    for apl in range(rg):
        t1=threading.Thread(target=thread,args=(apl,),name="t1")
        t1.start()



