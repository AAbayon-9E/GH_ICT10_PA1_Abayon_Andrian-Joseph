# friends and clubs
from pyscript import display

Basketball = {'Gur', 'Oscar', 'JM', 'Inigo', 'Brenton'}
Communicationarts = {'Yciar', 'Gino', 'Lawis', 'William', 'Carl', 'Shiloh', 'Joco'}

display (Basketball | Communicationarts, target='output') 
display (Basketball & Communicationarts, target='output') 
display (Basketball, target='output') 
display (Communicationarts, target='output') 
display (Basketball - Communicationarts, target='output')

