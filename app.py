import streamlit as st
from basparse import parser
from basinterp import Interpreter
import sys
import io

st.set_page_config(page_title="Mini PHP Interpreter", layout="centered")

st.title("Mini PHP Interpreter (PLY)")
st.write("Subset PHP menggunakan Lex & Yacc")

code = st.text_area(
    "Masukkan kode PHP:",
    value="""<?php
$a = 1;
$b = 2;

if ($a < $b) {
    echo "a lebih kecil";
}

?>""",
    height=250
)

if st.button("Run"):
    try:
        # Tangkap stdout
        old_stdout = sys.stdout
        sys.stdout = buffer = io.StringIO()

        ast = parser.parse(code)
        Interpreter().run(ast)

        sys.stdout = old_stdout
        output = buffer.getvalue()

        st.success("Berhasil dijalankan")
        st.code(output)

    except Exception as e:
        sys.stdout = old_stdout
        st.error(f"Error: {e}")
