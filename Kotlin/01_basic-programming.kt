// one line comment
/*
   block comment
*/

fun main(args : Array<String>){

      print("Enter a color: ")
      var color = readLine()

      var name: String="Name"

      var age1=(0..1000).random()
      var age2=(0..1001).random()

      var age = if (age1>age2) age1 else age2

      var greet = "Hello ${name} of      age ${age},       you are ".replace("\\s+".toRegex()," ")

      var old = if(age>700){
          println(greet+"old!")
      }else if(age>500) {
          println(greet+"getting old!")
      }else if (age in 15..30){
          println(greet+"teenager!")
      }else {
          println(greet+"young!")
      }

      when (age) {
          in 1..100 -> println("Age between 1 and 100")
          in 100..500 -> println("Age between 100 and 500")
          in 500..1000 -> println("Age between 100 and 500")
      }


      when(color){
          "Red" -> println("Color is red")
          "Blue" -> println("Color is blue")
          else -> println("Color is neither red nor blue")
      }



      var arr1 = arrayOf(13,"tst",true,null)
      for (x in arr1){
          print("${x} ") //print without line break
      }
      println()
      var arr1_rev = arr1.reversed()
      println("$arr1_rev")

      var arr2 = listOf<Int>(1,2,3,4,5)
      arr2.forEach(::print)
      println()
      println(arr2.sum())

      var arr2_mut = arr2.toMutableList()
      for (i in 1..10){
          arr2_mut.add(i)
      }
      println("$arr2_mut")
      var arr3 = arr2_mut.toMutableList()

      for (i in 0..9){
          arr2_mut[i]+=1
      }
      println("$arr2_mut")

      val combinedarr = arr3.plus(arr2_mut)
      println("$combinedarr")
}
