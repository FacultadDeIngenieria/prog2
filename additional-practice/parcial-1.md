---

title: Ejercicios adicionales - Parcial 1
layout: practice
permalink: /additional-practice/parcial-1
-----------------------------------------

# Ejercicios adicionales - Parcial 1

A continuación encontrarás una serie de ejercicios pensados para practicar Programación Orientada a Objetos en Java. Cada enunciado describe un problema que deberás modelar utilizando clases, objetos, encapsulamiento, recursividad y testing.

---

## Ejercicio 1 – Biblioteca Digital

### Instructions

Una biblioteca de barrio decidió informatizar el registro de sus libros y préstamos. Actualmente, cualquier persona que se haga socia puede retirar libros si están disponibles, y devolverlos cuando ya no los necesite. La biblioteca también quiere llevar un control de cuántos libros prestados tiene en un momento dado.

Debes modelar el sistema para que permita:

* Registrar socios.
* Manejar el estado de los libros (prestados o no).
* Permitir que un socio pida prestado y devuelva libros.
* Calcular el total de libros prestados mediante recursividad.
* Escribir al menos 2 tests que prueben el correcto funcionamiento de métodos distintos.

### Examples

* Un socio pide prestado un libro disponible → el libro queda marcado como prestado.
* Un socio devuelve un libro → el libro vuelve a estar disponible.
* El sistema consulta el total de libros prestados y devuelve el número correcto.

<details>
<summary>Mostrar solución en Java</summary>

```java
import java.util.ArrayList;
import java.util.List;

class Usuario {
    private String nombre;
    private List<Libro> librosPrestados = new ArrayList<>();
    public Usuario(String nombre) { this.nombre = nombre; }
    public void pedirPrestado(Libro libro) {
        if (!libro.estaPrestado()) {
            libro.prestar();
            librosPrestados.add(libro);
        }
    }
    public void devolver(Libro libro) {
        if (librosPrestados.contains(libro)) {
            libro.devolver();
            librosPrestados.remove(libro);
        }
    }
    public List<Libro> getLibrosPrestados() { return librosPrestados; }
}

class Libro {
    private String titulo;
    private boolean prestado;
    public Libro(String titulo) { this.titulo = titulo; this.prestado = false; }
    public void prestar() { prestado = true; }
    public void devolver() { prestado = false; }
    public boolean estaPrestado() { return prestado; }
}

class Biblioteca {
    private List<Libro> libros = new ArrayList<>();
    public void agregarLibro(Libro libro) { libros.add(libro); }
    public int totalLibrosPrestados() { return contarPrestados(libros, 0); }
    private int contarPrestados(List<Libro> libros, int index) {
        if (index >= libros.size()) return 0;
        return (libros.get(index).estaPrestado() ? 1 : 0) + contarPrestados(libros, index + 1);
    }
}
```

```java
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class BibliotecaTest {
    @Test
    void testPrestamoYDevolucion() {
        Biblioteca b = new Biblioteca();
        Libro l1 = new Libro("Libro A"); b.agregarLibro(l1);
        Usuario u = new Usuario("Ana");
        u.pedirPrestado(l1); assertTrue(l1.estaPrestado());
        u.devolver(l1); assertFalse(l1.estaPrestado());
    }

    @Test
    void testTotalLibrosPrestados() {
        Biblioteca b = new Biblioteca();
        Libro l1 = new Libro("Libro A");
        Libro l2 = new Libro("Libro B");
        b.agregarLibro(l1); b.agregarLibro(l2);
        Usuario u = new Usuario("Ana");
        u.pedirPrestado(l1);
        assertEquals(1, b.totalLibrosPrestados());
    }
}
```

</details>

---

## Ejercicio 2 – Tienda de Mascotas

### Instructions

Una tienda de mascotas vende diferentes animales (perros, gatos, hámsters, etc.) cada una con un precio diferente calculado sobre un precio base de 10.000,00 pesos. Cada mascota puede estar disponible para la venta o ya haber sido vendida. Los clientes que llegan a la tienda pueden comprar una mascota, siempre que no esté vendida. El dueño de la tienda quiere saber en cualquier momento cuántas mascotas se vendieron en total.

Los perros tienen un costo adicional por el mantenimiento de la tienda de mascotas, de un 20% el precio base por mascota. (20% de 10.000,00 = 2.000,00)

Los gatos están a mitad de precio de una mascota normal porque la tienda tiene demasiados.

Los Hamster valen un 10% de lo que sale una mascota normal, porque no requieren mucho mantenimiento.

Debes modelar el sistema para que permita:

* Registrar clientes.
* Manejar las mascotas de diferentes especies en venta y sus estados.
* Registrar la compra de mascotas por parte de los clientes.
* Calcular el total de mascotas vendidas con un método recursivo.
* Calcular el monto total en pesos de las ventas de mascotas.
* Escribir al menos 2 tests para verificar el correcto funcionamiento de métodos distintos.

### Examples

* Un cliente compra un perro → el perro pasa a estado "vendido".
* El sistema consulta el total de mascotas vendidas y devuelve el número correcto.

<details>
<summary>Mostrar solución en Java</summary>

```java
import java.util.ArrayList;
import java.util.List;

class Cliente {
    private String nombre;
    private List<Mascota> mascotasCompradas = new ArrayList<>();
    private double totalGastado = 0;
    public Cliente(String nombre) { this.nombre = nombre; }

    public void comprarMascota(Mascota mascota, double precioBase) {
        if(!mascota.estaVendida()){
            mascota.vender();
            mascotasCompradas.add(mascota);
            totalGastado += mascota.precioFinal(precioBase);
        }
    }

    public double getTotalGastado() { return totalGastado; }
    public List<Mascota> getMascotasCompradas() { return mascotasCompradas; }
}

abstract class Mascota {
    protected String nombre;
    protected boolean vendida;
    public Mascota(String nombre){ this.nombre = nombre; this.vendida = false; }
    public void vender(){ vendida = true; }
    public boolean estaVendida(){ return vendida; }
    public abstract double precioFinal(double precioBase);
}

class Perro extends Mascota {
    public Perro(String nombre){ super(nombre); }
    @Override
    public double precioFinal(double precioBase){ return precioBase * 1.2; } // +20%
}

class Gato extends Mascota {
    public Gato(String nombre){ super(nombre); }
    @Override
    public double precioFinal(double precioBase){ return precioBase * 0.5; } // 50% del precio base
}

class Hamster extends Mascota {
    public Hamster(String nombre){ super(nombre); }
    @Override
    public double precioFinal(double precioBase){ return precioBase * 0.1; } // 10% del precio base
}

class Tienda {
    private List<Mascota> mascotas = new ArrayList<>();
    public void agregarMascota(Mascota m){ mascotas.add(m); }

    public double totalVentas(double precioBase){ return contarVentas(mascotas, 0, precioBase); }

    private double contarVentas(List<Mascota> lista, int index, double precioBase){
        if(index >= lista.size()) return 0;
        Mascota m = lista.get(index);
        return (m.estaVendida()? m.precioFinal(precioBase) : 0) + contarVentas(lista,index+1,precioBase);
    }
}

```

```java
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class TiendaTest {
    @Test
    void testCompraMascotaYPrecio() {
        Tienda t = new Tienda();
        Mascota perro = new Perro("Fido");
        Mascota gato = new Gato("Michi");
        Mascota hamster = new Hamster("Chiqui");
        t.agregarMascota(perro); t.agregarMascota(gato); t.agregarMascota(hamster);

        Cliente c = new Cliente("Carlos");
        double precioBase = 100;

        c.comprarMascota(perro, precioBase);
        c.comprarMascota(gato, precioBase);
        c.comprarMascota(hamster, precioBase);

        assertEquals(100*1.2 + 100*0.5 + 100*0.1, c.getTotalGastado(), 0.001);
    }

    @Test
    void testTotalVentas() {
        Tienda t = new Tienda();
        Mascota perro = new Perro("Fido");
        Mascota gato = new Gato("Michi");
        t.agregarMascota(perro); t.agregarMascota(gato);

        double precioBase = 50;
        Cliente c = new Cliente("Ana");
        c.comprarMascota(perro, precioBase);

        assertEquals(50*1.2, t.totalVentas(precioBase), 0.001);
    }
}
```

</details>

---

# Ejercicio 3 – Plataforma de Cursos Online

### Instructions

Una plataforma de educación en línea quiere administrar las inscripciones de sus estudiantes. Cada curso, que puede ser online o presencial tiene un cupo máximo de inscriptos. Los estudiantes pueden anotarse en cursos mientras aún haya lugar. La plataforma también quiere conocer el número total de inscripciones hechas, calculado con un método recursivo.

Los cursos online, permiten que cualquier estudiante inscrito reciba automaticamente el certificado.

Los cursos presenciales, requiren que el estudiante haya asistido a todas las clases para poder generar el certificado.

Debes modelar el sistema para que permita:

* Registrar estudiantes.
* Crear cursos y controlar el cupo.
* Permitir la inscripción de estudiantes en cursos.
* Generar un certificado para los estudiantes que completan un curso.
* Organizar cursos en distintas categorías.
* Calcular de manera recursiva la cantidad total de inscripciones en la plataforma.
* Escribir al menos 2 tests que validen métodos distintos.

<details>
<summary>Mostrar solución en Java</summary>

```java
import java.util.ArrayList;
import java.util.List;

class Estudiante {
    private String nombre;
    public Estudiante(String nombre){ this.nombre = nombre; }
    public String getNombre(){ return nombre; }
}

abstract class Curso {
    protected String nombre;
    protected int cupo;
    protected List<Estudiante> inscritos = new ArrayList<>();

    public Curso(String nombre,int cupo){
        this.nombre = nombre;
        this.cupo = cupo;
    }

    public boolean inscribirEstudiante(Estudiante e){
        if(inscritos.size()<cupo){
            inscritos.add(e);
            return true;
        }
        return false;
    }

    public List<Estudiante> getInscritos(){ return inscritos; }

    // Cada tipo de curso define cómo generar el certificado
    public abstract boolean generarCertificado(Estudiante e);
}

class CursoOnline extends Curso {
    public CursoOnline(String nombre,int cupo){ super(nombre,cupo); }

    @Override
    public boolean generarCertificado(Estudiante e){
        // Los cursos online envían certificado automáticamente si está inscrito
        return inscritos.contains(e);
    }
}

class CursoPresencial extends Curso {
    private List<Estudiante> asistencias = new ArrayList<>();

    public CursoPresencial(String nombre,int cupo){ super(nombre,cupo); }

    public void registrarAsistencia(Estudiante e){
        if(inscritos.contains(e) && !asistencias.contains(e)){
            asistencias.add(e);
        }
    }

    @Override
    public boolean generarCertificado(Estudiante e){
        // Se genera certificado solo si asistió a todas las clases
        return asistencias.contains(e);
    }
}

class Plataforma {
    private List<Curso> cursos = new ArrayList<>();
    public void agregarCurso(Curso c){ cursos.add(c); }

    public int totalInscripciones(){ return contarInscripciones(cursos,0); }

    private int contarInscripciones(List<Curso> cursos,int index){
        if(index>=cursos.size()) return 0;
        return cursos.get(index).getInscritos().size() + contarInscripciones(cursos,index+1);
    }
}

// Tests
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class PlataformaTest{
    @Test
    void testInscripcionYCertificadoOnline(){
        Plataforma p = new Plataforma();
        CursoOnline co = new CursoOnline("Java",2); p.agregarCurso(co);
        Estudiante e = new Estudiante("Ana");
        assertTrue(co.inscribirEstudiante(e));
        // Generación de certificado online
        assertTrue(co.generarCertificado(e));
    }

    @Test
    void testCertificadoPresencialYTotalInscripciones(){
        Plataforma p = new Plataforma();
        CursoPresencial cp = new CursoPresencial("Python",2);
        Plataforma pl = new Plataforma();
        pl.agregarCurso(cp);

        Estudiante e1 = new Estudiante("Juan");
        Estudiante e2 = new Estudiante("Luis");

        cp.inscribirEstudiante(e1);
        cp.inscribirEstudiante(e2);

        // Solo el que asistió obtiene certificado
        cp.registrarAsistencia(e1);
        assertTrue(cp.generarCertificado(e1));
        assertFalse(cp.generarCertificado(e2));

        assertEquals(2, pl.totalInscripciones());
    }
}
```

</details>


---

# Ejercicio 4 – Cine

### Instructions

Un cine quiere registrar funciones, vender entradas y controlar el total de entradas vendidas. Los clientes pueden comprar entradas y se debe calcular recursivamente el total de ventas.

Debes modelar el sistema para que permita:

* Registrar clientes.
* Crear funciones de cine.
* Vender entradas a los clientes.
* Calcular el total de entradas vendidas usando un método recursivo.
* Escribir al menos 2 tests para validar métodos distintos.

<details>
<summary>Mostrar solución en Java</summary>

```java
import java.util.ArrayList;
import java.util.List;

class Cliente {
    private String nombre;
    public Cliente(String nombre) { this.nombre = nombre; }
    public String getNombre() { return nombre; }
}

class Funcion {
    private String pelicula;
    private int entradasDisponibles;
    private int entradasVendidas;

    public Funcion(String pelicula, int entradas) {
        this.pelicula = pelicula;
        this.entradasDisponibles = entradas;
        this.entradasVendidas = 0;
    }

    public boolean venderEntrada() {
        if (entradasDisponibles > 0) {
            entradasDisponibles--;
            entradasVendidas++;
            return true;
        }
        return false;
    }

    public int getEntradasVendidas() { return entradasVendidas; }
}

class Cine {
    private List<Funcion> funciones = new ArrayList<>();

    public void agregarFuncion(Funcion f) { funciones.add(f); }

    public int totalEntradasVendidas() { return contarEntradas(funciones, 0); }

    private int contarEntradas(List<Funcion> lista, int index) {
        if (index >= lista.size()) return 0;
        return lista.get(index).getEntradasVendidas() + contarEntradas(lista, index + 1);
    }
}

// Tests
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class CineTest {
    @Test
    void testVentaEntradas() {
        Cine cine = new Cine();
        Funcion f1 = new Funcion("Matrix", 2);
        Funcion f2 = new Funcion("Avatar", 3);
        cine.agregarFuncion(f1);
        cine.agregarFuncion(f2);

        f1.venderEntrada();
        f2.venderEntrada();
        f2.venderEntrada();

        assertEquals(3, cine.totalEntradasVendidas());
    }
}
```

</details>

---

# Ejercicio 5 – Supermercado

### Instructions

Un supermercado quiere registrar compras de clientes, manejar productos (que pueden ser perecederos o no perecederos) y calcular ingresos totales. Debe contar los productos distintos vendidos con un método recursivo.

Los productos perecederos, si se venden despues de su fecha de vencimiento, el precio baja un 50%.

Los productos perecederos, se se venden más de 5 unidades de ese producto, aplica un 10% de descuento por la cantidad comprada. Ejemplo: Si compras 10 unidades de un producto, el precio final es 90% del precio original. Si compras 15 unidades, el precio final es 85% del precio original. Si compras 20 unidades, el precio final es 80% del precio original.

Debes modelar el sistema para que permita:

* Registrar clientes y productos.
* Crear compras y agregarlas al historial.
* Calcular el ingreso total de todas las compras.
* Contar productos distintos vendidos usando recursión.
* Escribir al menos 2 tests que verifiquen métodos distintos.

<details>
<summary>Mostrar solución en Java</summary>

```java
import java.util.ArrayList;
import java.util.List;
import java.time.LocalDate;

abstract class Producto {
    protected String nombre;
    protected double precio;
    protected int stock;
    public Producto(String nombre,double precio,int stock){
        this.nombre = nombre; this.precio = precio; this.stock = stock;
    }
    public abstract double precioVenta(int cantidad);
    public boolean vender(int cantidad){
        if(cantidad <= stock){ stock -= cantidad; return true; }
        return false;
    }
    public String getNombre(){ return nombre; }
}

class ProductoPerecedero extends Producto {
    private LocalDate vencimiento;
    public ProductoPerecedero(String nombre,double precio,int stock,LocalDate vencimiento){
        super(nombre,precio,stock);
        this.vencimiento = vencimiento;
    }
    @Override
    public double precioVenta(int cantidad){
        double precioFinal = precio * cantidad;
        if(LocalDate.now().isAfter(vencimiento)) precioFinal *= 0.5; // 50% descuento si vencido
        return precioFinal;
    }
}

class ProductoNoPerecedero extends Producto {
    public ProductoNoPerecedero(String nombre,double precio,int stock){ super(nombre,precio,stock);}
    @Override
    public double precioVenta(int cantidad){
        double precioFinal = precio * cantidad;
        if(cantidad > 5) precioFinal *= 0.9; // 10% descuento por cantidad
        return precioFinal;
    }
}

class Cliente {
    private String nombre;
    public Cliente(String nombre){ this.nombre = nombre; }
}

class Compra {
    private Cliente cliente;
    private List<Producto> productos = new ArrayList<>();
    private List<Integer> cantidades = new ArrayList<>();

    public Compra(Cliente c){ this.cliente=c; }
    public void agregarProducto(Producto p, int cantidad){
        if(p.vender(cantidad)){ productos.add(p); cantidades.add(cantidad); }
    }

    public double total(){
        double suma = 0;
        for(int i=0;i<productos.size();i++){
            suma += productos.get(i).precioVenta(cantidades.get(i));
        }
        return suma;
    }

    public List<Producto> getProductos(){ return productos; }
}

class Supermercado {
    private List<Compra> historial = new ArrayList<>();
    public void registrarCompra(Compra c){ historial.add(c); }

    public double ingresoTotal(){
        double suma=0;
        for(Compra c: historial) suma += c.total();
        return suma;
    }

    public int productosDistintosVendidos(){
        return contarProductos(historial,0,new ArrayList<>());
    }

    private int contarProductos(List<Compra> compras,int index,List<String> nombres){
        if(index>=compras.size()) return nombres.size();
        for(Producto p: compras.get(index).getProductos()){
            if(!nombres.contains(p.getNombre())) nombres.add(p.getNombre());
        }
        return contarProductos(compras,index+1,nombres);
    }
}

// Testsimport org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
        import java.time.LocalDate;

class SupermercadoTest {
    @Test
    void testIngresoTotalYProductosDistintos() {
        Supermercado s = new Supermercado();
        Cliente c = new Cliente("Ana");

        Producto p1 = new ProductoPerecedero("Manzana",10,100, LocalDate.now().minusDays(1));
        Producto p2 = new ProductoNoPerecedero("Pan",5,50);

        Compra compra1 = new Compra(c);
        compra1.agregarProducto(p1,2); // vencido → precio 50% off
        compra1.agregarProducto(p2,6); // >5 unidades → 10% descuento

        s.registrarCompra(compra1);

        assertEquals(2*10*0.5 + 6*5*0.9, s.ingresoTotal(),0.001);
        assertEquals(2, s.productosDistintosVendidos());
    }

    @Test
    void testProductoNoPerecederoSinDescuento() {
        Supermercado s = new Supermercado();
        Cliente c = new Cliente("Juan");
        Producto p = new ProductoNoPerecedero("Galleta",2,10);
        Compra compra = new Compra(c);
        compra.agregarProducto(p,3); // menos de 5 → sin descuento
        s.registrarCompra(compra);

        assertEquals(3*2, s.ingresoTotal(),0.001);
        assertEquals(1, s.productosDistintosVendidos());
    }
}

```

</details>

