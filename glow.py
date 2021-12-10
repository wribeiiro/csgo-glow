import pymem
import pymem.process
import keyboard

dw_entity_list = 0x4DC178C
dw_local_player = 0xDA746C
m_iteam_num = 0xF4
dw_glow_object_manager = 0x5309C90
m_iglow_index = 0x10488

def main():
    process_manager = pymem.Pymem("csgo.exe")
    client = pymem.process.module_from_name(process_manager.process_handle, "client.dll").lpBaseOfDll

    while True:
        if keyboard.is_pressed("end"):
            exit(0)

        glow_manager = process_manager.read_int(client + dw_glow_object_manager)

        for i in range(1, 32):
            entity = process_manager.read_int(client + dw_entity_list + i * 0x10)

            if (entity):
                entity_team_id = process_manager.read_int(entity + m_iteam_num)
                entity_glow = process_manager.read_int(entity + m_iglow_index)

                # Terrorist
                if (entity_team_id == 2):
                    print("Terrorist")
                    process_manager.write_float(glow_manager + entity_glow * 0x38 + 0x8, float(1)) #R
                    process_manager.write_float(glow_manager + entity_glow * 0x38 + 0xC, float(0)) #G
                    process_manager.write_float(glow_manager + entity_glow * 0x38 + 0x10, float(0)) #B
                    process_manager.write_float(glow_manager + entity_glow * 0x38 + 0x14, float(1)) #A
                    process_manager.write_int(glow_manager + entity_glow * 0x38 + 0x28, 1) #Enabling

                # Counter-Terrorist
                if (entity_team_id == 3):
                    print("Counter-Terrorist")
                    process_manager.write_float(glow_manager + entity_glow * 0x38 + 0x8, float(0)) #R
                    process_manager.write_float(glow_manager + entity_glow * 0x38 + 0xC, float(0)) #G
                    process_manager.write_float(glow_manager + entity_glow * 0x38 + 0x10, float(1)) #B
                    process_manager.write_float(glow_manager + entity_glow * 0x38 + 0x14, float(1)) #A
                    process_manager.write_int(glow_manager + entity_glow * 0x38 + 0x28, 1) #Enabling

if __name__ == '__main__':
    main()