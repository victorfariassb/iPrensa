import base64
from base64 import b64encode
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Attachment, FileContent, FileName, FileType, Disposition, ContentId

from raspador_sites import coleta_globo, coleta_uol

def send_mail(dataframe, dataframe2):
    now = datetime.now()
    agora = now.strftime("%d/%m/%Y %H:%M:%S")

    # Defining Email Body and Notificaion type.    
    html_content=f'<b>Radar da Imprensa.</b><br> Seguem os dados de {agora}'

    # Defining Email_Format.
    message = Mail(
        from_email='victorfariassb@gmail.com',
        to_emails=['victorfariass@hotmail.com'],
        subject='test',
        html_content=html_content)
  
    base64_csv = b64encode(dataframe.to_csv(index=False, encoding='utf-8').encode()).decode()
    base64_2_csv = b64encode(dataframe.to_csv(index=False, encoding='utf-8').encode()).decode()

    anexo = Attachment(FileContent(base64_csv),
                                    FileName(f'{dataframe};{now.strftime("%d_%m_%Y_%Hh%Mm")}.csv'),
                                    FileType('text/csv'),
                                    Disposition('attachment'),
                                    ContentId('dataframe'))
    anexo2 = Attachment(FileContent(base64_2_csv),
                                    FileName(f'{dataframe2}{now.strftime("%d_%m_%Y_%Hh%Mm")}.csv'),
                                    FileType('text/csv'),
                                    Disposition('attachment'),
                                    ContentId('dataframe'))
    message.add_attachment(anexo)
    message.add_attachment(anexo2)

    
    try:
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        response = sg.send(message)
    except Exception as e:
        return e
    
    return None

uol = coleta_uol()
globo = coleta_globo()

send_mail(globo, uol)
