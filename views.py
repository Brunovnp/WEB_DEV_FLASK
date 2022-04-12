from flask import Flask, render_template, request, url_for
from app import app
from app import calculator as cl
import numpy as np
import webview



@app.route("/", methods=["GET", "POST"])
def index():

	if request.method == "POST":

		vp = float((request.form['valor']).replace('.','').replace(',','.'))
		i = float((request.form['tx_antc']).replace(',','.'))
		p = int(request.form['parcelas'])
		mq = int(request.form['cartao'])


		dados = cl.get_net(vp, i, p, mq)
		ns = range(len(dados))


		return render_template("index.html", ns=ns, dados=dados)

	else:
		return render_template("index.html")