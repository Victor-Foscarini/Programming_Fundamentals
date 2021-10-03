
fun main(args: Array<String>){

    //list
    var users = listOf<String>(
            "usr1",
            "usr2",
            "usr3",
            "usr4"
    )

    for ((index,name) in users.withIndex()){
        println("number ${index+1} name is $name.")
    }
    println()

    //map
    var usr = mutableMapOf<String,String>()
    usr["username"] = "user"
    usr["password"] = "pass"
    usr["email"] = "user@hotmail.com"

    for ((key,value) in usr){
        println("$key -> $value")
    }

}