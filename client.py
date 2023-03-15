import asyncio
from aioquic.asyncio import QuicConnectionProtocol
from aioquic.quic.configuration import QuicConfiguration
from aioquic.quic.connection import QuicConnection


async def main():
    loop = asyncio.get_running_loop()

    # Connect to the server
    config = QuicConfiguration(is_client=True)
    async with QuicConnection(
        configuration=config,
        session_ticket_handler=None,
    ) as conn:
        # Create a new file
        stream = conn.create_stream()
        stream.write("This is the contents of the new file.")
        await stream.drain()
        await stream.send_eof()


asyncio.run(main())
