import mysql.connector
import sshtunnel
import passwords

sshtunnel.SSH_TIMEOUT = 5.0
sshtunnel.TUNNEL_TIMEOUT = 5.0

with sshtunnel.SSHTunnelForwarder(
    ('ssh.pythonanywhere.com'),
    ssh_username=passwords.YTMD_ssh_username, ssh_password=passwords.YTMD_ssh_password,
    remote_bind_address=(passwords.YTMD_remote_bind_address, 3306)
) as tunnel:
    connection = mysql.connector.connect(
        user=passwords.YTMD_user, password=passwords.YTMD_password,
        host=passwords.YTMD_host, port=tunnel.local_bind_port,
        database=passwords.YTMD_database,
    )
    print(connection)
    connection.close()