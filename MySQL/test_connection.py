import mysql.connector
import sshtunnel

sshtunnel.SSH_TIMEOUT = 5.0
sshtunnel.TUNNEL_TIMEOUT = 5.0

with sshtunnel.SSHTunnelForwarder(
    ('ssh.pythonanywhere.com'),
    ssh_username='YTMD', ssh_password='YTMD@08052004',
    remote_bind_address=('YTMD.mysql.pythonanywhere-services.com', 3306)
) as tunnel:
    connection = mysql.connector.connect(
        user='YTMD', password='YTMD@08052004',
        host='127.0.0.1', port=tunnel.local_bind_port,
        database='YTMD$YTMD_DB',
    )
    print(connection)
    connection.close()