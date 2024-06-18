import base64

from connectToGoogle import connectToGoogle
from getEmails import getEmails
from getRawText import getRawText
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]


def main():
  """
  Shows basic usage of the Gmail API.
  Lists the user's Gmail labels.
  """
  try:
    # Call the Gmail API
    service = connectToGoogle("token1.json", "credentials.json", SCOPES)
    user = service.users()
    
    messages = getEmails(user)

    raw_emails = getRawText(user, messages)
    #print("Raw emails: ", raw_emails[0])

  except HttpError as error:
    # TODO(developer) - Handle errors from gmail API.
    print(f"An error occurred: {error}")


if __name__ == "__main__":
  main()


'''
  msg_raw:
Delivered-To: martntest@gmail.com
Received: by 2002:a05:6400:60cf:b0:257:d6ef:9388 with SMTP id km15csp1697048ecb;
        Sun, 16 Jun 2024 18:11:31 -0700 (PDT)
X-Received: by 2002:a25:ac10:0:b0:df4:e36b:e9 with SMTP id 3f1490d57ef6-dff154b5cd6mr7332235276.54.1718586691475;
        Sun, 16 Jun 2024 18:11:31 -0700 (PDT)
ARC-Seal: i=1; a=rsa-sha256; t=1718586691; cv=none;
        d=google.com; s=arc-20160816;
        b=cssh6KqXpoG6lx640/vJOQx2wrpj+mkBAnpgJJ566xOFIfBLgzCTiiQoKSZVut2nvh
         zxoD384HBFqP+RhLgvtc4OtMy4aOhKX5Pp6vVrPcvF4Y7f/xzCSpHBkHVpXWGdTW4DHD
         ECWqmkzFw9M9DC3VkIWXIqc6NOdmHdoFrsmhNcmXkQbXq4/NeK1RTe3unPC00ENaTQtW
         h8UbjJ9bsa7JCvkmBSwFHFIvL+B1fU0+qzHjWZqnQsSGabAvgbzuGSpVUqDnsi/FZNwb
         zfpj054lvvfc/6SEnnsZoCVAL6AxQ8w9YjAy2mOGcZBZs0vIKdRuj5tNzHxWdBWgUYQs
         demQ==
ARC-Message-Signature: i=1; a=rsa-sha256; c=relaxed/relaxed; d=google.com; s=arc-20160816;
        h=to:subject:message-id:date:from:mime-version:dkim-signature;
        bh=CkcoHfLfpUaqley4BMjSTVPIpZKs73aWVrdTnOTkrH8=;
        fh=DhFfiWK8xD+aUNmglJeoSp0LPfHasM6mgvAG29n9u0I=;
        b=DMC9E/fIN5X5P+mfok1hEgfeg4z0DkXJmlpQ1DnHGWQHKGp9YWpU5Xk67NjJLOMVhx
         uOVCzMesy37EeVJHoTcRr8SSyuyt1VELXbbS98jTGo9XyoSWqhDqX1HC4czYNoHGCdCB
         Zcnh5eciNMfg82VC8nv2DqNK8xgw6z5huplQFeXua/05I8jtblGk/I7sj3NbWm+4S86v
         f+8m+VdHjae5Z3X843UmWD3LpC7C/UJ0LkPONYWrzZl8pPn5HuHVnffv4BVejSBy9oNZ
         j+8/ys6aEHECBnJVwMLMpQ+SYIJ2SQpvOq62IcLTYNCSpeVvNIV8JjHcaz02PQ4xMIpr
         k3jQ==;
        dara=google.com
ARC-Authentication-Results: i=1; mx.google.com;
       dkim=pass header.i=@gmail.com header.s=20230601 header.b=AWQhzGmD;
       spf=pass (google.com: domain of matinqurban@gmail.com designates 209.85.220.41 as permitted sender) smtp.mailfrom=matinqurban@gmail.com;
       dmarc=pass (p=NONE sp=QUARANTINE dis=NONE) header.from=gmail.com;
       dara=pass header.i=@gmail.com
Return-Path: <matinqurban@gmail.com>
Received: from mail-sor-f41.google.com (mail-sor-f41.google.com. [209.85.220.41])
        by mx.google.com with SMTPS id 3f1490d57ef6-dff2d31487fsor1668488276.0.2024.06.16.18.11.31
        for <martntest@gmail.com>
        (Google Transport Security);
        Sun, 16 Jun 2024 18:11:31 -0700 (PDT)
Received-SPF: pass (google.com: domain of matinqurban@gmail.com designates 209.85.220.41 as permitted sender) client-ip=209.85.220.41;
Authentication-Results: mx.google.com;
       dkim=pass header.i=@gmail.com header.s=20230601 header.b=AWQhzGmD;
       spf=pass (google.com: domain of matinqurban@gmail.com designates 209.85.220.41 as permitted sender) smtp.mailfrom=matinqurban@gmail.com;
       dmarc=pass (p=NONE sp=QUARANTINE dis=NONE) header.from=gmail.com;
       dara=pass header.i=@gmail.com
DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed;
        d=gmail.com; s=20230601; t=1718586691; x=1719191491; dara=google.com;
        h=to:subject:message-id:date:from:mime-version:from:to:cc:subject
         :date:message-id:reply-to;
        bh=CkcoHfLfpUaqley4BMjSTVPIpZKs73aWVrdTnOTkrH8=;
        b=AWQhzGmDXZbaqEwbprBaXeQz56T0K3x003t6Yo5ViQvwRZ/6j0d1VNwUKBm5fPGlTG
         3AKqR5D7KzPGXWtkBVd5dYsPXaeUyaqbkdQiTrYcwc6Q9WJJTDNw38Gx4BCIrgHbd80k
         yvzvVqrBeTcwiSNKbSrM/2xOjLwtoMEdkwK4WaDh6+BhQMQJdCMsYkuVoGe+nnPPiiy1
         PB+o6ZO8iFJK/3+tPDJZtSqg++LwlKgwGHmY3NtbXNirx97hU5bZaoaxh6qhVxbP4zb5
         qt1s3hhgMAbwFV8ZtuHO+VryuP23NgJAkI6XtOrmrM/qCMccjZqEbSTnQzBWCWj1XVAi
         82mA==
X-Google-DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed;
        d=1e100.net; s=20230601; t=1718586691; x=1719191491;
        h=to:subject:message-id:date:from:mime-version:x-gm-message-state
         :from:to:cc:subject:date:message-id:reply-to;
        bh=CkcoHfLfpUaqley4BMjSTVPIpZKs73aWVrdTnOTkrH8=;
        b=EGryUywmRfFDVD1FmcoIlZBytFA9HCWRu89+hYIjlQaSlwUxoY2dOJB2kY4ntdQVla
         Vdn32s2bbkK33llvbQa9L4nsXFzx4ivg5f52igi/yjgIZ47xtyUO2tM4kqW5tMBXThTO
         LdJ95ov34a6e324y1JO8kpcyiI5L0mZlZRkvUMjyctUqxJgk5CkfU4CHHQPQI93ml/rj
         9Cyc5qBkxgH4URh86LaVWswZwdKw1vtLsOWi6dXBKkX25ziMaRbY6HI89NzDn2fx21ZC
         ksYKkVWbajadBK0ysIRfrGAOn7r4+WWLzXjt72O0kMZ9iRkuHfJvSIaUO8gbIufUiIEI
         JBIA==
X-Gm-Message-State: AOJu0YwTaNZAW3Ds03oyGYSZ6A+f4snXYDxmeCBIEM/MxsCKyz1ajro4
	K2YlIALsEWvWyoiDZT7O08lLS68xASk/8PWfXmsgfoHvNVVBTaYH/soSNSjbXVAG3SRXUuMoN3H
	Qwpkf6Q6CeMjsUj4o/TkPpHE7i3QM1g==
X-Google-Smtp-Source: AGHT+IEfeHr65qxOA96+oLuZil5L53BueiuCZJ+e2ZzQhApDJOHjOVprgg0pNeHZrdAWjCT9v5CdcqujmI1vQUswoNM=
X-Received: by 2002:a25:aa09:0:b0:dff:806:1388 with SMTP id
 3f1490d57ef6-dff15474e4bmr7691182276.46.1718586690798; Sun, 16 Jun 2024
 18:11:30 -0700 (PDT)
MIME-Version: 1.0
From: the legend of me <matinqurban@gmail.com>
Date: Sun, 16 Jun 2024 18:11:20 -0700
Message-ID: <CAE+gEmKWCT0ZZbhVRhcHvd_uOJDinM-2Qcxm+J9JNOa+eKp0dQ@mail.gmail.com>
Subject: test email
To: martntest@gmail.com
Content-Type: multipart/alternative; boundary="000000000000389261061b0ba56d"

--000000000000389261061b0ba56d
Content-Type: text/plain; charset="UTF-8"

Single line
second line

new line

*END*

--000000000000389261061b0ba56d
Content-Type: text/html; charset="UTF-8"
Content-Transfer-Encoding: quoted-printable

<div dir=3D"ltr">Single line<div>second line</div><div><br></div><div>new l=
ine=C2=A0</div><div><br></div><div><b>END</b></div></div>

--000000000000389261061b0ba56d--


'''