import asyncio
from aioquic.asyncio import QuicConnectionProtocol, serve


class FileCreationProtocol(QuicConnectionProtocol):
    async def handle_stream(self, stream):
        # Read the file contents from the stream
        file_contents = await stream.read()

        # Create the file with the contents
        with open("new_file.txt", "w") as file:
            file.write(file_contents)


async def main():
    loop = asyncio.get_running_loop()

    # Create the QUIC server
    server = await serve(
        loop=loop,
        port=4433,
        create_protocol=FileCreationProtocol,
        server_name="localhost",
        certificate_path="certificate.pem",
        private_key_path="key.pem",
    )

    await server.serve_forever()


asyncio.run(main())
