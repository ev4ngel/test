import httplib,urllib,urlparse
import re,json,datetime

def getRealUrlFromLink(link):
    '''
        from the given link we can get the file's real url
    '''
    rt=urllib.urlopen(link)
    try:
        rst=rt.read()
        r=re.search(r"encodeURIComponent\('(.*)'?\)",rst)
        if r!=None:
            return r.group(1)
        return -1
    except IOError:
        return None
def generateJsonFile(jf,jsonobj):
    jfo=open(jf+".json",'w')
    try:
        jfo.write(json.dumps(jsonobj,encoding="utf8"))
    finally:
        jfo.close()

def main():
    mDirt={}
    print("""
        XCrmS's Update.txt auto generator
            author:ev4n Gited!

                         
            Goooood Luck!
            """)
    version=raw_input("Input The Version(Like 1.0,2.6.3):")
    description=raw_input("Input Description:")
    apklink=raw_input("Input The Apk URL(Enter For None):")
    reslink=raw_input("Input The Res URL(None For What):")
    print("Waiting For Generating...")
    mDirt['ver']=version
    mDirt['des']=description.decode("GBK")
    mDirt['date']=datetime.date.today().strftime("%Y-%m-%d")
    mDirt['files']={}
    if apklink!="":
        mDirt['files']['apk']=getRealUrlFromLink(apklink)
    if reslink!="":
        mDirt['files']['res']=getRealUrlFromLink(reslink)
    generateJsonFile(version,mDirt)
    print("Done!")
if __name__=="__main__":
    main()   
