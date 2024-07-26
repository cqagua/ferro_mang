import streamlit_authenticator as stauth

# Senhas em texto claro (você pode mudar essas senhas)
passwords = ['capam2024', 'capam2024']

# Gerar hashes das senhas
hashed_passwords = stauth.Hasher(passwords).generate()

# Exibir os hashes gerados
for i, hash in enumerate(hashed_passwords):
    print(f"Hash for user{i+1}: {hash}")
    
#import version - modulo provavelmente atualizou 

    
