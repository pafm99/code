//
//  ViewController.m
//  Text Encryption
//
//  Created by Grzegorz Wójcik on 06.05.2015.
//  Copyright (c) 2015 Grzegorz Wójcik. All rights reserved.
//

#import "ViewController.h"
#import "TopCell.h"
#import "TextCell.h"
#import "PassCell.h"
#import "BottomCell.h"
#import "RMUniversalAlert.h"
#import <MessageUI/MessageUI.h>
#import "Base64_RC4.h"

#define TOP_CELL_H 70
#define BOTTOM_CELL_H 50
#define PASS_CELL_H 50
#define URL_SCHEME @"encrypted-text://"

#define TEXT_TAG 23
#define PASSWORD_TAG 43

#define DEFAULT_TEXT
@interface ViewController () <UITableViewDataSource, UITableViewDelegate,MFMessageComposeViewControllerDelegate,MFMailComposeViewControllerDelegate>
{
    NSString *msgFromURL;
}
@end

@implementation ViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    [self.tableView setSeparatorStyle:UITableViewCellSeparatorStyleNone];
    [self.tableView registerNib:[UINib nibWithNibName:@"TopCell" bundle:nil] forCellReuseIdentifier:@"TopCell"];
    [self.tableView registerNib:[UINib nibWithNibName:@"TextCell" bundle:nil] forCellReuseIdentifier:@"TextCell"];
    [self.tableView registerNib:[UINib nibWithNibName:@"BottomCell" bundle:nil] forCellReuseIdentifier:@"BottomCell"];
    [self.tableView registerNib:[UINib nibWithNibName:@"PassCell" bundle:nil] forCellReuseIdentifier:@"PassCell"];
    UITapGestureRecognizer *tap = [[UITapGestureRecognizer alloc] initWithTarget:self action:@selector(hideKeyboard)];
    [self.tableView addGestureRecognizer:tap];
    [self.view setBackgroundColor:[UIColor blackColor]];
    
    UIView* view = [[UIView alloc] initWithFrame:[[UIScreen mainScreen] bounds]];
    CAGradientLayer *gradient = [CAGradientLayer layer];
    gradient.frame = view.bounds;
    gradient.colors = [NSArray arrayWithObjects:(id)[[UIColor colorWithRed:0/255. green:237/255. blue:154/255. alpha:1.0] CGColor], (id)[[UIColor colorWithRed:0/255. green:139/255. blue:232/255. alpha:1.0] CGColor], nil];
    [view.layer insertSublayer:gradient atIndex:0];
    self.tableView.backgroundView = view;
    self.tableView.scrollEnabled = NO;
}
-(void)viewDidAppear:(BOOL)animated
{
    [super viewDidAppear:animated];
    if(msgFromURL)
        [self messageTextView].text = msgFromURL;
}

-(void)hideKeyboard
{
    [self.view endEditing:YES];
}

- (NSInteger)tableView:(UITableView *)tableView numberOfRowsInSection:(NSInteger)section {
    return 4;
}
-(CGFloat)calculateMiddleCellHeight
{
    CGRect rect=[[UIScreen mainScreen] bounds];
    return rect.size.height - TOP_CELL_H - BOTTOM_CELL_H - PASS_CELL_H;
}
-(CGFloat)tableView:(UITableView *)tableView heightForRowAtIndexPath:(NSIndexPath *)indexPath
{
    if(indexPath.row == 0)
        return TOP_CELL_H;
    if(indexPath.row == 1)
        return [self calculateMiddleCellHeight];
    if(indexPath.row == 2)
        return PASS_CELL_H;
    return BOTTOM_CELL_H;
}
- (UITableViewCell *)tableView:(UITableView *)tableView cellForRowAtIndexPath:(NSIndexPath *)indexPath {
    NSString *cellIdent = @"TopCell";
    if(indexPath.row == 1)
        cellIdent = @"TextCell";
    else if(indexPath.row == 2)
        cellIdent = @"PassCell";
    else if(indexPath.row == 3)
        cellIdent = @"BottomCell";
    
    UITableViewCell *cell = [tableView dequeueReusableCellWithIdentifier:cellIdent forIndexPath:indexPath];
    [cell setSelectionStyle:UITableViewCellSelectionStyleNone];
    cell.backgroundColor = [UIColor clearColor];
    switch (indexPath.row) {
        case 0:
        {
            TopCell *c = (TopCell*)cell;
            [c.clearBtn addTarget:self action:@selector(clearTouched:) forControlEvents:UIControlEventTouchUpInside];
            [c.cpyBtn addTarget:self action:@selector(copyPressed:) forControlEvents:UIControlEventTouchUpInside];
            [c.sendBtn addTarget:self action:@selector(sendBtnPressed) forControlEvents:UIControlEventTouchUpInside];
            break;
        }
        case 1:
        {
            TextCell *c = (TextCell*)cell;
            c.textView.tag = TEXT_TAG;
            break;
        }
        case 2:
        {
            PassCell *c = (PassCell*)cell;
            c.textField.tag = PASSWORD_TAG;
            break;
        }
        case 3:
        {
            BottomCell *c = (BottomCell*)cell;
            [c.encryptBtn addTarget:self action:@selector(encryptBtnPressed) forControlEvents:UIControlEventTouchUpInside];
            [c.decryptBtn addTarget:self action:@selector(decryptBtnPressed) forControlEvents:UIControlEventTouchUpInside];

            break;
        }
        default:
            break;
    }
    return cell;
}
-(void)sendBtnPressed
{
    [RMUniversalAlert showActionSheetInViewController:self
                                            withTitle:NSLocalizedString(@"Send",nil)
                                              message:NSLocalizedString(@"You can send encrypted text with:",nil)
                                    cancelButtonTitle:NSLocalizedString(@"Cancel",nil)
                               destructiveButtonTitle:nil
                                    otherButtonTitles:@[NSLocalizedString(@"SMS",nil), NSLocalizedString(@"E-Mail",nil)]
                   popoverPresentationControllerBlock:^(RMPopoverPresentationController *popover){
                                                           popover.sourceView = self.view;
                                                           popover.sourceRect = CGRectMake(self.view.bounds.size.width / 2.0, 80, 1.0, 1.0);
                                                       }
                                             tapBlock:^(RMUniversalAlert *alert, NSInteger buttonIndex){
                                                 if (buttonIndex == alert.firstOtherButtonIndex)
                                                     [self sendSms];
                                                 else if (buttonIndex == alert.firstOtherButtonIndex+1)
                                                     [self sendEmail];
                                                 
                                             }];
}
-(void)encryptBtnPressed
{
    if([self passwordTextField].text.length!=0){
        char *str= (char*)[[self messageTextView].text UTF8String];
        NSString *pass=[self passwordTextField].text;
        CRC4 rc4;
        rc4.Encrypt(str,[pass UTF8String] );
        
        CBase64  base64;
        char *dst;
        dst = (char*)malloc( base64.B64_length(strlen(str))+1);
        if(dst == NULL)
            return;
        
        base64.Encrypt(str,strlen(str),dst);
        NSString *wynik=[[NSString alloc]initWithCString:dst encoding:NSUTF8StringEncoding];
        [self messageTextView].text=wynik;
    }
    else{
        [RMUniversalAlert showAlertInViewController:self
                                          withTitle:NSLocalizedString(@"Password field is empty", nil)
                                            message:NSLocalizedString(@"Please enter password.", nil)
                                  cancelButtonTitle:@"OK"
                             destructiveButtonTitle:nil
                                  otherButtonTitles:nil
                                           tapBlock:nil];
    }
}
-(void)decryptBtnPressed
{
    if([self passwordTextField].text.length!=0){
        char *dst= (char*)[[self messageTextView].text UTF8String];
        char *str;
        str = (char*)malloc( [[self messageTextView].text length] );
        CBase64  base64;
        CRC4 rc4;
        base64.Decrypt(dst,strlen(dst),str);
        NSString *pass=[self passwordTextField].text;
        rc4.Decrypt(str,[pass UTF8String]);
        NSString *wynik=[[NSString alloc]initWithCString:str encoding:NSUTF8StringEncoding];
        if(wynik.length==0){
            [RMUniversalAlert showAlertInViewController:self
                                              withTitle:NSLocalizedString(@"No results", nil)
                                                message:NSLocalizedString(@"Check if your password is correct.", nil)
                                      cancelButtonTitle:@"OK"
                                 destructiveButtonTitle:nil
                                      otherButtonTitles:nil
                                               tapBlock:nil];
        }
        else
            [self messageTextView].text=wynik;
    }
    else{
        [RMUniversalAlert showAlertInViewController:self
                                          withTitle:NSLocalizedString(@"Password field is empty", nil)
                                            message:NSLocalizedString(@"Please enter password.", nil)
                                  cancelButtonTitle:@"OK"
                             destructiveButtonTitle:nil
                                  otherButtonTitles:nil
                                           tapBlock:nil];
    }
}

-(void)sendSms
{
    if([[UIApplication sharedApplication] canOpenURL:[NSURL URLWithString:@"tel://"]]==YES){
        MFMessageComposeViewController *controller = [[MFMessageComposeViewController alloc] init];
        if([MFMessageComposeViewController canSendText])
        {
            controller.body = [URL_SCHEME stringByAppendingString:[self messageTextView].text];
            controller.messageComposeDelegate = self;
            [self presentViewController:controller animated:YES completion:nil];
        }
    }
    else{
        [RMUniversalAlert showAlertInViewController:self
                                          withTitle:NSLocalizedString(@"Can't send SMS", nil)
                                            message:NSLocalizedString(@"This device doesn't support sending SMS.", nil)
                                  cancelButtonTitle:@"OK"
                             destructiveButtonTitle:nil
                                  otherButtonTitles:nil
                                           tapBlock:nil];
    }
}
-(void)sendEmail
{
    MFMailComposeViewController *picker = [[MFMailComposeViewController alloc] init];
    picker.mailComposeDelegate = self;
    NSString *adres=@"<a href=\"https://itunes.apple.com/us/app/text-encryption-hidden-messages/id992934796\">Text Encryption</a>";
    NSString *url=[NSString stringWithFormat:@"Text encrypted with %@. Tap on it, to decrypt:<br>%@",adres,[URL_SCHEME stringByAppendingString:[self messageTextView].text]];
    [picker setMessageBody:url isHTML:YES];
    
    [self presentViewController:picker animated:YES completion:nil];
}
- (void)mailComposeController:(MFMailComposeViewController *)controller
          didFinishWithResult:(MFMailComposeResult)result
                        error:(NSError *)error {
    [self dismissViewControllerAnimated:YES completion:nil];
}
- (void)messageComposeViewController:(MFMessageComposeViewController *)controller didFinishWithResult:(MessageComposeResult)result
{
    [self dismissViewControllerAnimated:YES completion:nil];
}


-(UITextView*)messageTextView
{
    return (UITextView*)[self.tableView viewWithTag:TEXT_TAG];
}
-(UITextField*)passwordTextField
{
    return (UITextField*)[self.tableView viewWithTag:PASSWORD_TAG];
}

-(IBAction)copyPressed:(id)sender
{
    UIPasteboard *pasteboard = [UIPasteboard generalPasteboard];
    NSString *w=[URL_SCHEME stringByAppendingString:[self messageTextView].text];
    pasteboard.string=w;
    
    [RMUniversalAlert showAlertInViewController:self
                                      withTitle:NSLocalizedString(@"Copied", nil)
                                        message:NSLocalizedString(@"Copied to clipboard.", nil)
                              cancelButtonTitle:@"OK"
                         destructiveButtonTitle:nil
                              otherButtonTitles:nil
                                       tapBlock:nil];
}

-(IBAction)clearTouched:(id)sender
{
    [RMUniversalAlert showAlertInViewController:self
                                      withTitle:NSLocalizedString(@"Clear", nil)
                                        message:NSLocalizedString(@"Are you sure?", nil)
                              cancelButtonTitle:NSLocalizedString(@"Cancel",nil)
                         destructiveButtonTitle:NSLocalizedString(@"Clear",nil)
                              otherButtonTitles:nil
                                       tapBlock:^(RMUniversalAlert *alert, NSInteger buttonIndex){
                                           if (buttonIndex >= alert.destructiveButtonIndex) {
                                               [self messageTextView].text = NSLocalizedString(@"Enter here text for encryption/decryption...",nil);
                                           }
                                       }];

}


-(void)loadTextFromURL:(NSString*)msg
{
    UITextView *tv = [self messageTextView];
    msg = [msg stringByReplacingOccurrencesOfString:URL_SCHEME withString:@""];
    if(!tv)
    {
        msgFromURL = msg;
    }
    else
        tv.text = msg;
}

- (void)willAnimateRotationToInterfaceOrientation:(UIInterfaceOrientation)toInterfaceOrientation duration:(NSTimeInterval)duration
{
    // resize your layers based on the view’s new bounds
    [[[self.tableView.backgroundView.layer sublayers] objectAtIndex:0] setFrame:[[UIScreen mainScreen] bounds]];
}
- (BOOL)prefersStatusBarHidden
{
    return NO;
}

@end
