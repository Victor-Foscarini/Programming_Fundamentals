
fun greetings(){
    println("Function acessed")
}

fun findSquare(a: Int){
    println(a*a)
}

fun getSum(numbers: List<Int>) : Int {
    return numbers.sum()
}

fun add(a: Int, b : Int) : Int = a+b

fun Sum(numbers: List<Int>) : Int = numbers.sum()

fun max(a: Int,b: Int): Int = if (a>b) a else b

fun main(args: Array<String>){

    greetings()
    findSquare(5)

    var numbers = listOf<Int>(1,2,3,4)
    println(getSum(numbers))
    println(Sum(numbers))

    println(add(2,4))
    println(max(2,4))

}