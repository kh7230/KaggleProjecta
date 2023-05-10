# -*- coding:utf-8 -*-
import streamlit as st
from streamlit_option_menu import option_menu
from description import run_description
from eda import run_eda
from ml_app import run_ml_app
from stats import run_stat

def main(run_lecture=None):
    with st.sidebar:
        selected = option_menu("Main Menu", ['Home', 'Description', 'Data', 'EDA','ML_APP', 'STAT','LECTURE'],
                icons=['house', 'card-checklist', 'card-checklist', 'bar-chart', 'clipboard-data'],
                menu_icon="cast", default_index=0, orientation = 'vertical')

    if selected == 'Description':
        run_description()
    elif selected == 'Data':
        pass
    elif selected == 'EDA':
        run_eda()
    elif selected == 'ML_APP':
        run_ml_app()
    elif selected == 'STAT':
        run_stat()
    elif selected == 'LECTURE':
        run_lecture()
    else:
        print('error..')


if __name__ == "__main__":
    main()