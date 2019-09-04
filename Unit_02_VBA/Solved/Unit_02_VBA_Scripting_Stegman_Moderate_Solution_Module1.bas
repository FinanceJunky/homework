Attribute VB_Name = "Stegman_Module1"
'Moderate Solution
Sub fun_with_stocks()

'Define Variables
Dim ticker As String
Dim next_ticker As String
Dim yearly_percent_change As Double
Dim init_open As Double
Dim final_close As Double
Dim volume As Double
Dim total_counter As Integer
Dim counter As Long
Dim last_row As Long

ticker = "A"


For Each ws In ActiveWorkbook.Worksheets
    
    'Set initial values
    total_counter = 1
    counter = 0
    init_open = 0
    volume = 0
    
    'Format Header
    Cells(total_counter, 9).Value = "Ticker"
    Cells(total_counter, 10).Value = "Yearly Change"
    Cells(total_counter, 11).Value = "Percent Change"
    Cells(total_counter, 12).Value = "Total Stock Volume"
    
    Columns("I:L").AutoFit
    
    last_row = ActiveSheet.Cells(Rows.Count, "A").End(xlUp).Row

    MsgBox last_row
    
    'Loop
    For i = 2 To last_row
    
        
        'Set ticker, next_ticker
        ticker = Cells(i, 1).Value
        next_ticker = Cells(i + 1, 1).Value
                
        'Set init_open, final_close price values and display values
        If next_ticker <> ticker Then
                    
            final_close = (Cells(i, 6).Value)
            init_open = (Cells(i - counter, 3).Value)
            total_counter = (total_counter + 1)
            Cells(total_counter, 9).Value = (ticker)
            Cells(total_counter, 10).Value = ((CDbl(final_close)) - (CDbl(init_open)))
            'Ticker Plnt values are 0 for 2015 and 2014
            If init_open = 0 Then
                Cells(total_counter, 11).Value = "Undefined"
            Else
                Cells(total_counter, 11).Value = (((CDbl(final_close)) - (CDbl(init_open))) / (CDbl(init_open)))
            End If
            'Formating
            If (Cells(total_counter, 10).Value < 0) Then
                Cells(total_counter, 10).Interior.ColorIndex = 3
            Else
                Cells(total_counter, 10).Interior.ColorIndex = 4
            End If
            
            'Add final volume
            volume = (CDbl(volume) + CDbl(Cells(i, 7).Value))
            
            Cells(total_counter, 12).Value = volume
        
            'reset variables
            counter = 0
            volume = 0
        
        Else
            'Increase counter and add trading volume
            counter = counter + 1
            volume = (CDbl(volume) + CDbl(Cells(i, 7).Value))
                
            
        End If

        
    Next i
    
    'Formatting
    Range("K:K").NumberFormat = "0.00%"


    If ws.Index < (Worksheets.Count) Then
        ActiveSheet.Next.Select
    End If

Next ws

End Sub



