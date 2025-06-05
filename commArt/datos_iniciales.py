from Modelos.Comision import Comision
from Modelos.Mensaje import Mensaje
from extensiones import db
from Modelos.Usuario import Usuario
from Modelos.Artista import Artista
from Modelos.Categoria import Categoria
from Modelos.Publicacion import Publicacion
from datetime import datetime, date
from werkzeug.security import generate_password_hash

def insertar_datos(app):
    with app.app_context():
        # Verificamos si ya existen usuarios (Comprueba si ya hay datos)
        if Usuario.query.first():
            print("Datos iniciales ya insertados.")
            return

        # ---------- Crear Usuarios ----------
        u1 = Usuario(
            correo="blingBlosh@example.com",
            username="Mister_blingBlos34",
            descripcion="¡Hola gentesilla! Soy Mister BlingBlos, ilustrador especializado en paisajes realistas y escenarios de fantasía. Si te gustan los cielos imposibles, las montañas que susurran leyendas o los bosques donde parece que vive algo mágico… probablemente te interese lo que hago.\n\nTrabajo creando fondos, escenarios conceptuales, y paisajes que se sienten vivos. Ideal para juegos, novelas visuales o simplemente decorar tu espacio.\n\n💸 Precios orientativos:\nFondo simple : 40 €\nPaisaje detallado: 70–90 €\nConcept art para entornos: desde 100 €\n\nMe encanta trabajar con descripciones detalladas como si estuviera leyendo una novela. Si tienes una idea, puedo construirle un mundo alrededor :).",
            contrasenia=generate_password_hash("1234"),  # Con hash implementado
            fecha_nacimiento=datetime(2000, 5, 1),
            activo=True
        )
        u2 = Usuario(
            correo="miriam362@example.com",
            username="Casual_Gamer456",
            descripcion = "Aloo soy Miriam, desarrolladora de videojuegos indie. Me paso el día entre líneas de código, mecánicas raras y mundos imaginarios. Para darles forma, suelo encargar animaciones, sprites y assets visuales que los hagan brillar.\n\nUso esta app para conectar con artistas que puedan traducir ideas técnicas en arte con personalidad. Si haces pixel art, animación 2D o ilustraciones de personajes… ¡me interesa tu trabajo!\n\n🔧 No soy artista, pero sí muy clara con lo que necesito: briefs bien hechos, referencias listas y feedback constructivo. ¡Si colaboramos espero que me trateis bien! (Suelo ser muy perfeccionista)",
            contrasenia=generate_password_hash("4321"),
            fecha_nacimiento=datetime(1995, 8, 15),
            activo=True
        )
        u3 = Usuario(
            correo="windyyys@example.com",
            username="WindyAnimales",
            descripcion="Holiiii soy Windy y mi arte gira en torno a lo bonito, lo suave y adorable (GATOS). Dibujar animales adorables y criaturas fantásticas de mirada tierna es mi pasión.\n\nTrabajo con comisiones personalizadas, desde retratos de mascotas hasta criaturas inventadas. \n\n💸 Precios de referencia:\nRetrato de mascota: $20 USD\nAnimalito (inventado o real): $35–50 USD\nIlustración personalizada: desde $60 USD\n\nSoy súper detallista y pongo mucho cariño en cada trazo. ¡No hay nada que una buena dosis de ternura no pueda mejorar! 🐶🌼",
            contrasenia=generate_password_hash("pelusa02/12"),
            fecha_nacimiento=datetime(1990, 8, 5),
            activo=True
        )
        u4 = Usuario(
            correo="Gickia@example.com",
            username="geckos_chan",
            descripcion= "Holi uwu. Soy geckos_chan, furro orgulloso y gecko-identificado desde tiempos prehistóricos. Alma reptiliana atrapada en un cuerpo humano desde 2009 (bueno, más o menos).\n\nNo dibujo, pero sí encargo... mucho.  Soy fan número uno de todo lo que tenga escamas, garras o colitas que se menean. Aquí estoy para seguir a mis artistas favoritos, apoyar commissions y encargar arte de mi fursona gecko vestida como si fuera al Met Gala.\n\n💸 Spoiler: tengo mucho dinero y me encanta consentir a mis artistas favoritos 7v7. Si haces arte que grite \"esto pertenece en una galería furry interdimensional\", probablemente ya estés en mi radar 0w0.\n\nAsí que sí, soy un gecko con gustos caros. Y no, no me arrepiento. 🦎✨",
            contrasenia=generate_password_hash("ImAGeckoSoWhat"),
            fecha_nacimiento=datetime(2009, 1, 23),
            activo=True
        )

        db.session.add_all([u1, u2, u3, u4])
        db.session.commit()

        # ---------- Crear Artista ----------
        a1 = Artista(id_artista=u1.id_usuario)
        a2 = Artista(id_artista=u3.id_usuario)
        db.session.add_all([a1, a2])
        db.session.commit()

        # ---------- Crear Categorías ----------
        #Para insertar categorias mas rapido hacemos un buble con una lista
        categorias = [Categoria(nombre_categoria=n) for n in ["pixelart", "chibi", "realismo", "animales", "fantasia", "abstracto", "animacion", "collage", "paisajes", "sprites", "anime", "retrato"]]
        db.session.add_all(categorias)
        db.session.commit()

        # ---------- Asignar Categorías al artista ----------
        #Gracias al mapeo asignamos directamente a categorias las categorias que queremos
        a1.categorias.extend([categorias[3], categorias[9]])
        a2.categorias.extend([categorias[4], categorias[3], categorias[2]])
        db.session.commit()

        # ---------- Crear Publicaciones ----------
        pub1 = Publicacion(
            dibujo="img/paisaje.jpg",
            descripcion_publicacion="Hola mundo! Esta es mi primera publicación espero que le deis mucho amor <3\n\nMe ha llevado 3 días acabar esta pintura pero ha merecido totalmente la pena.\nMe encantó el resultado!!",
            num_likes=2,
            fecha_publicacion=date(2020,12,3),
            id_artista_publicacion=a1.id_artista
        )
        pub2 = Publicacion(
            dibujo="img/pelusa.jpg",
            descripcion_publicacion="Uff primera publicación eh. \nUna mañana me levanté y vi a mi gato mirando por la ventana, como si estuviera teniendo flashbacks de Vietnam, con esos ojos azules tan bonitos que te miran hasta el alma. \nAsí que pensé en dibujarlo, y la verdad es que me encantó el resultado. \nEs un dibujo algo viejo, pero creo que es perfecto como carta de presentación.",
            num_likes=3,
            fecha_publicacion=date(2023,8,12),
            id_artista_publicacion=a2.id_artista
        )
        pub3 = Publicacion(
            dibujo="img/chibi.png",
            descripcion_publicacion="Hooolaaa :D. Hoy me levanté con ganas de experimentar, así que, gente, os presento mi primer chibi. \n¡Quedó súper mono, eee! Lo añadiré como parte de mis tags, por si acaso... a lo mejor me sale mejor de lo que esperaba.",
            num_likes=1,
            fecha_publicacion=date(2024,11,21),
            id_artista_publicacion=a2.id_artista
        )
        db.session.add_all([pub1, pub2, pub3])
        db.session.commit()

        # ---------- Seguidos de los users ----------
        u1.seguidos.append(u2)
        u1.seguidos.append(u3)
        u2.seguidos.append(u1)
        u4.seguidos.append(u2)
        u4.seguidos.append(u3)
        db.session.commit()

        # ---------- Comisiones ----------
        com1 = Comision(
            descripcion_com="Holaa buenasss hace poco estuve de visita en grecia y los monumentos de alli me dejaron sin palabras. \n¿Sería posible si me hicieras un dibujo de un paisaje romano? me da igual como sea lo dejo a tu eleccion. \nSimplemente quería algo así para colgarlo en mi sala de estar. Gracias!!",
            dibujo="img/paisaje_griego.jpg",
            estado="Terminada",
            tipo="Individual",
            fecha_creacion=date(2021,7,17),
            id_cliente_com=u2.id_usuario,
            id_artista_com=a1.id_artista
        )
        com2 = Comision(
            descripcion_com="Hola me gustaría que hicieras un dibujo de mi gato. ¿Se podría? Lo querría a digital a poder ser, así es más fácil de transportar jajjajaj.\n\nMi gato se llama Nube y es de tamaño mediano, de pelaje blanco suave, con manchas grises sobre el lomo y la cabeza. Tiene unos ojos grandes color ámbar y orejas puntiagudas. Su cola es larga, mullida y se mueve con una elegancia que solo él entiende. De hecho, cuando se acurruca parece una bolita de nieve mullidita.",
            dibujo=None,
            estado="En espera",
            tipo="Individual",
            fecha_creacion=date(2025,5,19),
            id_cliente_com=u1.id_usuario,
            id_artista_com=a2.id_artista
        )
        com3 = Comision(
            descripcion_com="Holisss oye ¿aceptas comisiones furras? \nMi oc es un Cyrtodactylus australotitiwangsaensis :3 tengo dinero MUCHO",
            dibujo=None,
            estado="En espera",
            tipo="Individual",
            fecha_creacion=date(2025,6,1),
            id_cliente_com=u4.id_usuario,
            id_artista_com=a2.id_artista
        )
        com4 = Comision(
            descripcion_com="Busco a un artista que sepa hacer animaciones para videojuegos. \nEstoy haciendo mi propio juego al estilo cyberpunk y todavía no sé cómo hacer mi personaje principal, así que necesito ayuda con esto!!\nMientras sepas hacer sprites y lo cyberpunk sea lo tuyo, me vale.\n\nRepito: TEMÁTICA ESTILO CYBERPUNK Y QUE SEPA HACER SPRITES. \nEs urgente, así que no tengo tiempo —por así decirlo— para que alguien que no haya hecho esta temática antes se apunte, plis.",
            dibujo=None,
            estado="En espera",
            tipo="Global",
            fecha_creacion=date(2025,6,3),
            id_cliente_com=u2.id_usuario,
            id_artista_com=None
        )
        db.session.add_all([com1, com2, com3, com4])
        db.session.commit()

        # ---------- Mensajes ----------
        msg1 = Mensaje(
            texto="¡Hola! Me interesa la comisión. Entonces esta es libre no quieres nada en especifico? Solo que sea un paisaje griego no?",
            id_user_creador=u1.id_usuario,
            id_com_asociada=com1.id_com
        )
        msg2 = Mensaje(
            texto="Holaaa siii eres libre de hacer lo que quieras!!",
            id_user_creador=u2.id_usuario,
            id_com_asociada=com1.id_com
        )
        msg3 = Mensaje(
            texto="Aaa pero con una condición que el paisaje sea antiguo en plan de la antigua grecia como era antes y no ahora",
            id_user_creador=u2.id_usuario,
            id_com_asociada=com1.id_com
        )
        msg4 = Mensaje(
            texto="Jajaja sin problema así más divertido!! Me pondré a ello",
            id_user_creador=u1.id_usuario,
            id_com_asociada=com1.id_com
        )
        com1.mensajes.append(msg1)
        com1.mensajes.append(msg2)
        com1.mensajes.append(msg3)
        com1.mensajes.append(msg4)
        db.session.commit()


print("✅ Datos iniciales insertados correctamente.")
