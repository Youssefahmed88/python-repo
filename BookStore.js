let bookstore = [
    { BookId: 1, BookTitle: 'Start with why', author: 'Simon Sinek', price: 80.0, quantity: 13 },
    { BookId: 2, BookTitle: 'But how do it know', author: 'J. Clark Scott', price: 120.0, quantity: 22 },
    { BookId: 3, BookTitle: 'Clean Code', author: 'Robert Cecil Martin', price: 50.0, quantity: 5 },
    { BookId: 4, BookTitle: 'Zero to One', author: 'Peter Thiel', price: 45.0, quantity: 12 },
    { BookId: 5, BookTitle: 'You don\'t know JS', author: 'Kyle Simpson', price: 90.0, quantity: 9 }
];
function add(id, title, author, price, quantity) {
    NewBook={
        
        'BookId':id,
        'BookTitle':title,
        'author':author,
        'price':price,
        'quantity':quantity
    }
    bookstore.push(NewBook);
    console.log(`${title} added successfully.`);
};

function edit(eid, etitle, eauthor, eprice, equantity) {
    const index=findBookIndex(eid)
    if (index !== -1) {
        bookstore[index].BookId=eid || bookstore[index].BookId
        bookstore[index].BookTitle=etitle || bookstore[index].BookTitle
        bookstore[index].author=eauthor || bookstore[index].author
        bookstore[index].price=eprice || bookstore[index].price
        bookstore[index].quantity=equantity || bookstore[index].quantity
        console.log('Book information updated successfully.')
    }
    else {
        console.log('Book not found.')
    }
}

function bookdel(id)
{
    const index = findBookIndex(id);

    if (index !== -1) {
        bookstore.splice(index, 1);
        console.log('Book deleted successfully.');
    } else {
        console.log('Book not found.');
    }
}

function display() {
    for (let i=0; i<bookstore.length; i++) {
        console.log(`
            Book Id: ${bookstore[i].BookId}
            Title: ${bookstore[i].BookTitle}
            Author: ${bookstore[i].author}
            Price: ${bookstore[i].price}
            Quantity: ${bookstore[i].quantity}
        `)
    }
}

function sell(title, QuantityToBuy, balance) {
    const index = findBookIndex(title);

    if (index !== -1){
        if (bookstore[index].quantity > 0 && QuantityToBuy <= bookstore[index].quantity){
            const TotalCost=bookstore[index].price * QuantityToBuy

            if (balance >= TotalCost){
                bookstore[index].quantity -=QuantityToBuy

                reciept(bookstore[index], QuantityToBuy, TotalCost);
            }
            else{
                console.log('Insufficient customer balance.');
            }
        }
        else{
            console.log('Insufficient quantity in stock.');
        }
    }
    else{
        console.log('Book not found.');
    }
}

function reciept(book, quantity, totalCost) {
    console.log('\nWelcome to Book Store\n');
    console.log('Receipt:');
    console.log('--------------------------------------');
    console.log(`Book Title: ${book.BookTitle}`);
    console.log(`Author: ${book.author}`);
    console.log(`Quantity: ${quantity}`);
    console.log(`Total Cost: ${totalCost}`);
    console.log('--------------------------------------')
    console.log('Thanks for your Visit, see you again')
};

function findBookIndex(check){
    for (let i=0;  i<bookstore.length; i++){
        if (bookstore[i].BookId==check || bookstore[i].BookTitle==check){
            return i;
        }
    }
    return -1;
}

while (true) {
    const prompt = require('prompt-sync')();
    let action = parseInt(prompt('\n1.Add 2.Edit 3.Delete 4.Display 5.Buy 6.Exit: ')); 
    if (action==6)
    {
       break;
    }
    else{

        switch(action) {
        
            case 1:
                let id=prompt('ID: ');
                let title=prompt('Title: ')
                let author=prompt('Author: ')
                let price=prompt('Price: ')
                let quality=prompt('Quantity: ')
                add(id, title, author, price, quality)
                break;
        
            case 2:
                let eid=prompt('ID: ');
                let etitle=prompt('Title: ')
                let eauthor=prompt('Author: ')
                let eprice=prompt('Price: ')
                let equantity=prompt('Quantity: ')
                
                edit(eid, etitle, eauthor, eprice, equantity)
                break;
        
            case 3:
                let delid = prompt('Enter Book Id to delete: ');
                    bookdel(delid);
                    break;
            case 4:
                display()
                break;
            case 5:
                let sellTitle=prompt('Title: ')
                let sellQuantity=prompt('Quantity: ')
                let customerBalance = prompt('Enter customer balance: ');
        
                sell(sellTitle, sellQuantity, customerBalance);
                break;
        
            default:
                console.log('Invalid action.');
        }   
    }
};
