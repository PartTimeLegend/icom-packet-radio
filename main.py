def main():
    from IcomRadioDetector import IcomRadioDetector
    from RadioController import RadioController

    print("Detecting Icom radios...")
    detector = IcomRadioDetector()
    radios = detector.detect_radios()

    if not radios:
        print("No Icom radios detected.")
        return

    print("Found Icom radios:")
    for i, port in enumerate(radios, 1):
        print(f"{i}. {port}")

    selected_index = (
        int(input("Enter the index of the Icom radio you want to use: ")) - 1
    )
    if selected_index < 0 or selected_index >= len(radios):
        print("Invalid index.")
        return

    selected_port = radios[selected_index]
    print(f"Selected port: {selected_port}")

    radio_controller = RadioController(selected_port)

    try:
        while True:
            packet_data = input("Enter packet data to send: ")
            radio_controller.send_packet_data(packet_data)

            received_data = radio_controller.receive_packet_data()
            print(f"Received packet data: {received_data}")

            more_data = input("Do you want to send more packet data? (y/n): ")
            if more_data.lower() != "y":
                break
    except KeyboardInterrupt:
        print("Exiting...")
    finally:
        radio_controller.close()


if __name__ == "__main__":
    main()
