library(ggplot2)
library(scales)
library(gridExtra)
library(RColorBrewer)
multicolor <- brewer.pal(5, "Set2") 

List_partecipants= function(a,b) {
  Partecipanti <- data.frame(
	User=unlist(b)
     )
  Title <- paste("\n Elenco partecipanti al corso: \n",unlist(a))
  colnames(Partecipanti) <- ("Nome e cognome")
  grid.arrange(top=Title,tableGrob(Partecipanti))

   
  }

Stat1 = function(a) {
  data <- data.frame(
  Courses=unlist(a)
 )
  barplot(table(data$Courses),ylab="Courses",xlab="Parteipanti", main="Numero iscritto per Coursi", xlim=c(0,10),
		horiz=T, border="#69b3a2",col=multicolor)
}

Stat2 = function(a,b) {
  data <- data.frame(
   Courses=unlist(a)
  )
  slices <- unlist(b)*as.vector(table(data$Courses))
  lbls <- names(table(data$Courses))
  pct <- round(slices/sum(slices)*100)
  lbls <- paste(lbls,pct)
  lbls <- paste(lbls,"%","\n",slices,"\u20AC",sep="")
  pie(slices, labels = lbls, main="Guadagno totale per Coursi",col=multicolor)
}

Stat3 = function(a) {
  data <- data.frame(
   Instructors=unlist(a)
  )
  barplot(table(data$Instructors),xlab="Nomi istruttori",ylab="Numero di Coursi tenuti", main="Courses tenuti per istruttore",ylim=c(0,10), border="#69b3a2",col=multicolor)

}

Stat4 = function(a) {
  dates <- data.frame(
		Date=unlist(a)
		)
  dates$Date <- as.POSIXct(dates$Date)
  p <- ggplot(dates, aes(Date,..count..)) + 
	   ylab("Numero iscritti") + 
		geom_histogram(bins=30,fill='green') +
		scale_x_datetime(breaks = date_breaks("1 months"),labels = date_format("%d-%b"), limits = c(as.POSIXct("2021-01-20"),as.POSIXct("2021-12-20")))+
		theme(axis.text.x=element_text(angle=45,hjust = 1, vjust = 1)) 
	print(p)

}


Stat5 = function(a,b) {
  gender <- unlist(a)
  birth_date <- unlist(b)
  birth_date <- as.Date(birth_date,  format = "%d/%m/%Y")
  age <-  as.numeric(difftime(Sys.Date(), birth_date, units = "weeks"))/52.25
  grp <- cut(age, breaks = seq(0, 90, 10))
  Users <- data.frame(age,gender,grp)
  rownames(Users) <- NULL
  Users <-Users[order(Users$age),]

  print(Users)
  p <-   ggplot(data=Users,aes(x=as.factor(grp),fill=gender)) + 
         geom_bar(data=subset(Users,gender=="F")) + 
	     geom_bar(data=subset(Users,gender=="M"),aes(y=..count..*(-1))) + 
         scale_y_continuous(breaks=seq(-10,10,1),labels=abs(seq(-10,10,1))) + 
		 labs(title = "Numero iscritti per sesso ed eta",y="Numero iscritti",x="Eta",fill="Sesso")+
     	 coord_flip()
	
  print(p)

  }







