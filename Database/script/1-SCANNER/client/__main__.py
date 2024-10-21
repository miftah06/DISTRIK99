# import sys
# import numpy as np
import pandas as pd
import emails as pd_emails
from matimeja import url as phonet
import dono as twitt

def get_data(telenet):
    df = pd.DataFrame(telenet)
    df.columns = ["emails", "phone", "ip"]
    return df


class Decode:
    print(" ISI EMAIL DI DALAM COLUM EMAIL DI SCRIPT INI SEBELUM EKSEKUSI YA!")
    pd_emails = None

    def __init__(self):
        self.df = pd.DataFrame()
        self.df["email"]="http://twitter.com/"
    pass


class emails():
    phonet = None

    def __init__(self):
        self.pd_emails = pd_emails
        nyaris = dono.url(self.pd_emails)
        self.df = pd.DataFrame()
        self.df["email"]=get_data(nyaris)
        self.df["phone"] = phonet.phone_number()
        self.df["ip"] = "127.0.0.1"
        self.df["email_id"] = self.df["email"].apply(lambda x : x.email)
        self.df["phone_id"] = self.df["phone"].apply(lambda x
                                                     : phonet.phone_number())
        self.df["ip_id"] = self.df["ip"].apply(lambda x
                                               : phonet.phone_number())
        self.df["email_id"] = self.df["email"].apply(lambda x
                                                     : phonet.email_address())
        self.df["phone_id"] = self.df["phone"].apply(lambda x
                                                     : phonet.phone_number())
        self.df["ip_id"] = self.df["ip"].apply(lambda x
                                               : phonet.phone_number())
        self.df["email_id"] = self.df["email"].apply(lambda x
                                                     : phonet.email_address())
        self.df["phone_id"] = self.df["phone"].apply(lambda x
                                                     : phonet.phone_number())
        self.df["ip_id"] = self.df["ip"].apply(lambda x
                                               : phonet.phone_number())
        self.df["email_id"] = self.df["email"].apply(lambda x
                                                     : phonet.email_address())
        self.df["phone_id"] = self.df["phone"].apply(lambda x
                                                     : phonet.phone_number())
        self.df["ip_id"] = self.df["ip"].apply(lambda x
                                               : phonet.phone_number())
        self.df["email_id"] = self.df["email"].apply(lambda x:x)

    def __init__(pd_emails, self=None):
        URLS = twitt.write(phonet.np, pd_emails)
        self.df = pd.DataFrame(URLS)


try:
    while (Decode != emails.phonet.decode ):
        with open(pd_emails, 'rb') as f:
            with open(output, 'w') as f1:
                print(f.write(pd_emails))
                print(f1.write(Decode.pd_emails))
except:
    print(" silahkan cek status akun tersebut")
    print("done ya kak")
    pass

