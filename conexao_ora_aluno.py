import oracledb

def conectar_oracle():
    user = 'rm569041'
    dsn = 'oracle.fiap.com.br:1521/orcl'
    password = input('Informe a sua senha: ')
    try:
        conn = oracledb.connect(user=user, dsn=dsn, password=password)
        print('Conexão estabelecida com sucesso!')
        return conn
    except:
        print('Erro ao conectar ao oracle!')
        return None

def testar_conexao():
    conn = conectar_oracle()
    if conn:
        cursor = conn.cursor()
        cursor.execute('SELECT sysdate FROM dual')
        resultado = cursor.fetchone()
        print(f'Teste OK! {resultado[0]}')
        cursor.close()
        conn.close()

if __name__ == '__main__':
    testar_conexao()