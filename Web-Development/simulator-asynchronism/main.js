const button = document.getElementById("btn");
const contenedor_general = document.querySelector(".contenedor_general");
const parrafo_producto = document.querySelector(".parrafo_producto");
const parrafo_precio = document.querySelector("parrafo_precio");

// arreglo de productos
let productos_tecnológicos = [
    {
        nombre: "Laptop HP",
        precio: 3500
    },
    {
        nombre: "Tablet Samsung",
        precio: 500
    },
    {
        nombre: "Iphone X",
        precio: 4500
    },
    {
        nombre: "Reloj Digital",
        precio: 400
    },
    {
        nombre: "Play Station 5",
        precio: 4000
    },
    {
        nombre: "Smart TV Samsung QLED 8k",
        precio: 4500
    }
];

const obtenerProductos = (id) => {
    return new Promise((resolve) => {
        if (typeof (productos_tecnológicos[id]) === "object") {
            setTimeout(() => {
                resolve(productos_tecnológicos[id])
            }, 500);
        } else {
            Promise.reject("Sucedió un error, el dato en el arreglo no es un objeto");
        }
    });
}


async function mostrarInformacion() {
    contenedor_general.innerHTML = "";
    for (let i = 0; i < productos_tecnológicos.length; i++) {
        let producto = await obtenerProductos(i);
        contenedor_general.innerHTML += `
        <div class="contenedor_producto">
            <div class="contenedor_parrafo">
                <p class="parrafo_producto"><b>Producto:</b> ${producto.nombre}</p>
            </div>
            <div class="contenedor_precio">
                <p class="parrafo_precio"><b>Precio:</b> ${producto.precio} soles</p>
            </div>
        </div>
        `;
    }
};


button.addEventListener("click", () => {
    mostrarInformacion();
})