#s = "     HelloWorld=1325659asdafew;  acidweadfwfe=af2659****"
class StringToJSON:
    def __init__(self,string,eqFlag = "=",EndFalg = ";"):
        self.string = string
        self.eqFlag = eqFlag
        self.endFlag = EndFalg
    def deleteBlack(self):
        while(not self.string.find(" ") == -1):
            self.string = self.string[:self.string.find(" ")]+ self.string[self.string.find(" ")+1:]
        self.string+=';'
    def extractToJson(self):
        self.deleteBlack()
        mode = 0
        keyBeginIndex = 0
        keyEndIndex = 0
        valueBeginIndex = 0
        valueEndIndex = 0
        result = {}
        for index,char in enumerate(self.string):
            if(mode == 0):
                if(char == self.eqFlag):
                    keyEndIndex = index
                    valueBeginIndex = index+1
                    mode = 1
            elif(mode == 1):
                if(char == self.endFlag):
                    valueEndIndex = index
                    result.update({self.string[keyBeginIndex:keyEndIndex]:self.string[valueBeginIndex:valueEndIndex]})
                    keyBeginIndex = index+1
                    mode = 0
        return result
if __name__ == "__main__":
    eqFlag = "="
    endFlag = ":"
    s = "UM_distinctid=171f231033b73-08907fd88315a2-29703570-9c4c8-171f231033c60; YUEDU_LOGIN=d429497b376e93002bb26246fce13701; NETEASE_WDA_UID=d429497b376e93002bb26246fce13701#|#1529209691725; YUEDU_LAST_LOGIN=d429497b376e93002bb26246fce13701#6; YUEDU_V_DID=1588906668621132; JSESSIONID-WYYD=3c7edf1a0f1ebb423fb109d7973c67ff23ac0b0d8328e3e220f273b017a50aae258ed43eaf59b328c11116c48ab8cf7428392a9cfe4e175840a40d11a6e0961873ace53c25ce49161b4e1926107679a05a72fbcb4a0e9382a7962d5ce11fbea9f400bd66bcd82ac12239d6b32a19ac3bf58cfac0963ef5269cfed6e815cbf7a8ef89e384; _ydklxeinuq_=23; XSRF-TOKEN=c6979cbe-e8c8-4f49-9d81-4fa5d8c5013a; davisit=1; __da_ntes_utmfc=utmcsr%3D(direct)%7Cutmccn%3D(direct)%7Cutmcmd%3D(none); NTES_YD_SESS=iwXClt_40w8Dl0gNrxYRltkMm9f2ZKwi29VbUu1BxVuf5CnFOwbg6tnPo1RDzWLs8uDfZ.dUi2Y8KUfO6RyqZEHV6HXJD5Re1L2m9JI3jhAsHYWCd7b3eUzW7KLSuo2BzZrYd5vvRC0zOsvHeSwYfZpPMV9a3CSvZfsL.NzpecqqVzBVddxRFCy.McsZ4avAMhXGlztfvaYFGr1vexY8yuTcM2c3BkZUdchqUfArttrXq; STAR_YD_SESS=iwXClt_40w8Dl0gNrxYRltkMm9f2ZKwi29VbUu1BxVuf5CnFOwbg6tnPo1RDzWLs8uDfZ.dUi2Y8KUfO6RyqZEHV6HXJD5Re1L2m9JI3jhAsHYWCd7b3eUzW7KLSuo2BzZrYd5vvRC0zOsvHeSwYfZpPMV9a3CSvZfsL.NzpecqqVzBVddxRFCy.McsZ4avAMhXGlztfvaYFGr1vexY8yuTcM2c3BkZUdchqUfArttrXq; _rom.us.c.v.ol=dx0RKis2FUwcJ3sqACsME1pSBUtHQkhUZA5TeVhZXxdOcVwcURpVeUpHWgY44785c3a; YUEDU_TD_CHANNEL=0cYp92in7; SDK_AUTH_=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1aWQiOiJZbVJsTnpGbVpXSmtNR1l5WkRNek5tWTJaakkzTURnMU1EQm1ZMkk0WkRFIiwiYXBwS2V5IjoiMGNZcDkyaW43IiwiZXh0ZW5kSW5mbyI6ImFFMDFXWEJ0TnpVNVoxTmxSV0pDUmpoMlRGTndjbE14U3pScVozUlRhaTlxVmpKM0wyY3lObmxqTDJSNFRXOWhkV1pWVERWVVZYRjVNVE5YVkdGRGEySjFkMmhaZEdoNk5UVndNVFY2YUVGUk0yOUVkMnRsY2pSNVMxUjBXakU1ZVRGbVdsZ3dibU56WmxOVU9EQkRSalpGV1daTFFYVjFOekpoTkhReGJrUklaa2t6Y0hjMk5YRnRNekU1UWxjNGJrVndOV1Z1ZVd0RVQxVXhaRTFZUWtsMFVtY3JkWHBFWkVOalBRIiwiaWF0IjoxNTg5MDAyMTY1fQ.luzxfz80U0lf0hyP8PBOVMlZwys9cPPcM3eaRxT6Das; READER_U_SDK_=dGFWAnSoL9Z6uejeHrCQXs6g7U8OTlRt3BFx6ySEgTgxZaiq8vrUwEMTU4OTAwMjE2ODA5NA1_N_URS; __da_ntes_utma=133183383.643289298.1588906541.1588916014.1589002717.3; __da_ntes_utmz=133183383.1588906541.1.1.utmcsr%3D(direct)%7Cutmccn%3D(direct)%7Cutmcmd%3D(none)"
    op = StringToJSON(s)
    print(op.extractToJson())
