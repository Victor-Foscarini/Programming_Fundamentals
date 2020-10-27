class User(email: String) {

    init {
        println("Inited")
    }

    constructor(id: String,email: String, name: String,password: String ) : this(email){
        println(id)
        println(name)
        println(password)
        println(email)
    }

}

fun main(args: Array<String>) {

    var belal = User("b2020_54","belk@gmail.com", "belk","12345")

}