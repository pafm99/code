function bdayCountDown(daysUntilMyBirthday){
    while (daysUntilMyBirthday > 5){
      console.log("There are ", daysUntilMyBirthday, "Days until my birthday. Such a long time... :(")
      daysUntilMyBirthday--;
      } 
    while (daysUntilMyBirthday > 0){
      console.log("THERE ARE ", daysUntilMyBirthday, "DAYS UNTIL MY BIRTHDAY!!")
      daysUntilMyBirthday--;
      } if (daysUntilMyBirthday === 0){
          console.log(` ♪ღ♪*•.¸¸¸.•*¨¨*•.¸¸¸.•*•♪ღ♪¸.•*¨¨*•.¸¸¸.•*•♪ღ♪•*
          ♪ღ♪░H░A░P░P░Y░ B░I░R░T░H░D░A░Y░░♪ღ♪
          *•♪ღ♪*•.¸¸¸.•*¨¨*•.¸¸¸.•*•♪¸.•*¨¨*•.¸¸¸.•*•♪ღ♪•«`)
      }
  }
  bdayCountDown(20);