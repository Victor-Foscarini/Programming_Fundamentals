class Hero {

    var nickName : String = ""
    fun findSquare(a : Double) : Double = Math.pow(a,2.0)
    fun sum(a : Int,b : Int) : Int = a+b

}

fun main(args : Array<String>){

    var spidey = Hero()
    spidey.nickName = "Parker"

    var ironMan = Hero()
    ironMan.nickName = "Stark"

    println(spidey.nickName)
    println(ironMan.nickName)

}