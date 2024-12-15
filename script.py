import obspython as obs

print("First Time")

# Global variables
timer_duration = 3600  # Default duration in seconds

# Function called when the timer executes


def stop_recording():
    obs.script_log(obs.LOG_INFO, "Timer Executed.")
    obs.obs_frontend_recording_stop()

    # Remover el temporizador para evitar que vuelva a ejecutarse
    obs.timer_remove(stop_recording)

# Function to start/reset the timer


def start_timer():
    obs.script_log(obs.LOG_INFO, f"Starting timer with duration: {
                   timer_duration} seconds.")
    obs.timer_remove(stop_recording)  # Remove any existing timer
    obs.timer_add(stop_recording, timer_duration * 1000)

# OBS UI properties setup


def script_properties():
    obs.script_log(obs.LOG_INFO, "Setting up script properties.")
    props = obs.obs_properties_create()
    obs.obs_properties_add_int(
        # Input for duration in minutes
        props, "duration", "Duración (minutos):", 1, 1440, 1)
    return props

# Called when the user updates the script properties


def script_update(settings):
    global timer_duration
    obs.script_log(obs.LOG_INFO, "Updating script settings.")
    timer_duration = obs.obs_data_get_int(
        settings, "duration") * 60  # Convert minutes to seconds
    start_timer()

# Called when the script is loaded


def script_load(settings):
    obs.script_log(obs.LOG_INFO, "Script loaded successfully.")
    start_timer()

# Script description


def script_description():
    return "Prueba básica de script en OBS con un temporizador configurable."


# import obspython as obs
# print("First Time")

# # Variable global
# timer_duration = 15  # Duración en segundos

# # Función que se llama cuando el temporizador finaliza


# def stop_recording():
#     obs.script_log(obs.LOG_INFO, "Timer Executed.")
#     obs.script_log(obs.LOG_INFO, str(timer_duration))

#     obs.obs_frontend_recording_stop()

# # Función que configura el temporizador


# def start_timer():
#     global timer_duration
#     obs.script_log(obs.LOG_INFO, "Run start_timer.")
#     obs.timer_add(stop_recording, timer_duration * 1000)

# # Interfaz de usuario en OBS


# def script_properties():
#     obs.script_log(obs.LOG_INFO, "Run script_properties.")

#     props = obs.obs_properties_create()
#     obs.obs_properties_add_int(
#         props, "duration", "Duración (minutos):", 1, 1440, 1)
#     return props

# # Se llama cuando el usuario cambia propiedades


# def script_update(settings):
#     global timer_duration
#     obs.script_log(obs.LOG_INFO, "Run script_update.")
#     timer_duration = obs.obs_data_get_int(settings, "duration") * 60
#     obs.timer_remove(start_timer)
#     start_timer()


# # # Valores por defecto
# # def script_defaults(settings):
# #     obs.obs_data_set_default_int(settings, "duration", 20)


# def script_description():
#     obs.script_log(obs.LOG_INFO, "Loading script_description.")
#     return "Prueba básica de script en OBS."

# # Se llama al cargar el script


# def script_load(settings):
#     obs.script_log(obs.LOG_INFO, "El script ha iniciado correctamente.")
#     start_timer()
