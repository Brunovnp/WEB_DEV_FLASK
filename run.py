from flask import Flask, render_template, request, url_for
from app import app
from app import calculator as cl
import numpy as np
import webview


windows = webview.create_window("Calculadora de Recebíveis", app, min_size=(1000, 1200))



if __name__ == '__main__':
    webview.start()











