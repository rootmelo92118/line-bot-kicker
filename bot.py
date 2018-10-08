from Linephu.linepy import *
from Linephu.akad.ttypes import *
import time
from time import sleep


client = LINE()
client.log("Auth Token : " + str(client.authToken))

oepoll = OEPoll(client)

MySelf = client.getProfile()
print("My MID : " + MySelf.mid)

invtag = []


def NOTIFIED_INVITE_INTO_GROUP(op):
    try:
        client.acceptGroupInvitation(op.param1)
        invtag.append(op.param2)
        client.sendMessage(op.param1, "bye bye")
    except Exception as e:
        print(e)
        print("\n\nNOTIFIED_INVITE_INTO_GROUP\n\n")
        return
    
    
def SEND_MESSAGE(op):
    msg = op.message
    try:
        if msg.toType == 2:
            if msg.contentType == 0:
                if msg.text == "bye bye":
                    print("start destroying")
                    _name = msg.text.replace("bye bye","")
                    group = client.getGroup(msg.to)
                    group.name = "幻滅之遺境"
                    client.updateGroup(group)
                    targets = []
                    for g in group.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        client.leaveGroup(msg.to)
                    else:
                        for target in targets:
                            try:
                                if target in invtag:
                                    pass
                                else:
                                    client.kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                            except:
                               group = client.getGroup(op.param1)
                               groupinvitingmembersmid = [contact.mid for contact in group.invitee]
                               for _mid in groupinvitingmembersmid:
                                   client.cancelGroupInvitation(op.param1, [_mid])
                                   time.sleep(0.5)
                    client.leaveGroup(msg.to)
        else:
            pass
        
    except Exception as e:
        print(e)
        print("\n\nSEND_MESSAGE\n\n")
        return
    
oepoll.addOpInterruptWithDict({
    OpType.NOTIFIED_INVITE_INTO_GROUP: NOTIFIED_INVITE_INTO_GROUP,
    OpType.SEND_MESSAGE: SEND_MESSAGE
})


while True:
    oepoll.trace()
