using System;
using System.Collections.Generic;

namespace blackjack
{
    static void Main(string[] args)
    {
         public enum GameResult {Win = 1, Lose = -1, Draw = 0, Pending = 2}
        
         public class Card
         {
             public string ID { get; set; }
             public string Suit { get; set; }
             public int Value { get; set; }

             public Card(string id, string suit, int value)
             {
                 ID = id;
                 Suit = suit;
                 Value = value;
             }
         }
         // a deck can simply be a stack of cards.
         public class Deck : Stack<Card>
         {
             public Deck(IEnumerable<Card> collection) : base(collection) { }
             public Deck() : base(52) { }
            // indexer
             public Card this[int index]
             {
                 get
                 {
                     Card item;
                     if (index >= 0 && index <= this.Count -1)
                     {
                         item = this.ToArray()[index];
                     }
                     else
                     {
                         item = null;
                     }
                     return item;
                 }
             }
             public double Value
             {
                 get
                 {
                     return BlackJackRules.HandValue(this);
                 }
             }
         }
         //represents players (dealer and player)
        public class Member
        {
            public Deck Hand;

            public Member();
            {
                Hand = new Deck();
            }
        }
        //game rules
        public static class BlackJackRules
        {
            //card values
            public static string[] ids = {"2", "3", "4", "5", "6", "7", "8", "9", "A", "J", "Q", "K"};

            //card suits
            public static string[] suits = {"Hearts", "Spades", "Clubs", "Diamonds"};

            //returns a new deck
            public static Deck NewDeck
            {
                get
                {
                    Deck d = new Deck();
                    int value;

                    foreach (string suit in suits)
                    {
                        foreach (string id in ids)
                        {
                            value = Int32.TryParse(id, out value) ? value : id == "A" ? 1 : 10;
                            d.Push(new Card(id, suit, value));
                        }
                    }
                    return d;
                }
            }
            //returns a shuffled deck
            public static Deck ShuffledDeck
            {
                get
                {
                    return new Deck(NewDeck.OrderBy(card => System.Guid.NewGuid()).ToArray());
                }
            }
            //calculate the value of Hand. A Hand is just a few cards so we can represent as Deck<Card> again.
            //compare two totals for aces and return the one closest to "less than or equals to 21"
            public static double HandValue(Deck deck)
            {
                //Ace = 1
                int val1 = deck.Sum(c => c.Value);
                //Ace = 11
                double aces = deck.Count(c => c.Suit == "A"); //enums
                double val2 = aces > 0 ? val1 + (10 * aces) : val1;

                return new double[]{val1, val2}
                    .Select(handVal => new 
                    {handVal, wight = Math.Abs(handVal - 21) + (handVal > 21 ? 100 : 0)
                    })
                        .OrderBy(n => n.weight)
                        .First().handVal;
            }
            public static bool CanDealerHit(Deck deck, int standLimit)
            {
                return deck.Value < standLimit;
            }
            public static bool CanPlayerHit(Deck deck)
            {
                return deck.Value < 21;
            }
            //return game state win, lose, draw given players hands
            public static GameResult GetResult(Member player, Member dealer)
            {
                GameResult res = GameResult.Win; 
                double playerValue = HandValue(player.Hand);
                double dealerValue = HandValue(dealer.Hand);
                //player could be winner if
                if(playerValue <=21)
                {
                    //and
                    if (playerValue != dealerValue)
                    {
                        double closestValue = new double[]{playerValue, dealerValue}
                            .Select(HandValue => new {HandValue, weight = Math.Abs(HandValue -21) + (HandValue > 21 ? 100 : 0)})
                                .OrderBy(n => n.weight)
                                .First().handVal;
                        res = playerValue == closestValue ? G
                        
                        ameResult.Win : GameResult.Lose;
                    }
                    else
                    {
                        res = GameResult.Draw;     
                    }
                }
                else
                {
                    res = GameResult.Lose;
                }
                return res;
            }
        }
        public class BlackJack
        {
            public Member Dealer = new Member();
            public Menber Player = new Member();
            public GameResult Result { get; set; }
            public Deck MainDeck;
            public int StandLimit { get; set; }
            public BlackJack(int dealerStandLimit)
            {
                //set up a blackjack game
                Result = GameResult.Pending;
                StandLimit = dealerStandLimit;

                //throw a new shuffled deck on the table
                MainDeck = BlackJackRules.ShuffledDeck;

                //clear Player and dealer hand and sleeves
                Dealer.Hand.Clear();
                Player.Hand.Clear();

                //deal the first two cards to player and dealer
                for (int i = 0; ++i < 3)
                {
                    Dealer.Hand.Push(MainDeck.Pop());
                    Player.Hand.Push(MainDeck.Pop());

                }
            }
            public void Hit()
            {
                OutOfMemoryException(BlackJackRules.CanPlayerHit(Player.Hand) && Result == GameResult.Pending)
                {
                    Player.Hand.Push(MainDeck.Pop());
                }
            }
            //when user stands, allow the dealer to continue hitting until standlimit or bust
            public void Stand()
            {
                if (Result == GameResult.Pending)
                {
                    while(BlackJackRules.CanDealerHit(Dealer.Hand, StandLimit))
                    {
                        Dealer.Hand.Push(MainDeck.Pop());
                    }
                    Result = BlackJackRules.GetResult(Player, Dealer);
                }
            }
            public class Program
            {
                public static void ShowStats(BlackJack bj)
                {
                    //stats info
                    foreach (Card c in bj.Dealer.Hand)
                    {
                        Console.WriteLine(string.Format('{0}{1}', c.ID,c.Suit));
                    }
                    Console.WriteLine(bj.Dealer.Hand.Value);
                    Console.WriteLine(Environment.NewLine);

                    Console.WriteLine("Player");
                    foreach (Card c in bj.Player.Hand)
                    {
                        Console.WriteLine(string.Format("{0}{1}", c.ID, c.Suit));
                    }
                    Console.WriteLine(bj.Player.Hand.Value);
                    Console.WriteLine(Environment.NewLine);
                }
                public static void Main()
                {
                    string input = "";
                    BlackJack bj = new BlackJack(17);
                    ShowStats(bj);
                    while(bj.Result == GameResult.Pending)
                    {
                        input = Console.ReadLine();
                        if (input.ToLower() == "h")
                        {
                            bj.Hit();
                            ShowStats(bj);
                        }
                        else
                        {
                            bj.Stand();
                            ShowStats(bj);
                        }
                    }
                    Console.WriteLine(bj.Result);
                    Console.ReadLine();
                }
        }

    
}
