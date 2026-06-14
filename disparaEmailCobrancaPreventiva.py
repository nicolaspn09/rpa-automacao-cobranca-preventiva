from datetime import datetime
from datetime import timedelta
import locale
import cx_Oracle
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import pandas as pd
import mysql.connector
import os
from openpyxl import Workbook, load_workbook

#Dispara e-mails para os clientes
def envia_email(mensagemEmail, destinatarios_email, codigo_cliente, setor_cliente):
    pass # Logica de negocio removida por seguranca corporativa


def envia_email_final(destinatarios_email_final, anexo, data_convertida):
    pass # Logica de negocio removida por seguranca corporativa

def conecta_sql():
    pass # Logica de negocio removida por seguranca corporativa

def consulta_notas_enviar_email():

    pass # Logica de negocio removida por seguranca corporativa
