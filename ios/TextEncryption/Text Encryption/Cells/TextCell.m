//
//  TextCell.m
//  Text Encryption
//
//  Created by Grzegorz Wójcik on 06.05.2015.
//  Copyright (c) 2015 Grzegorz Wójcik. All rights reserved.
//

#import "TextCell.h"

@implementation TextCell

- (void)awakeFromNib {
    //_textView.layer.borderColor = [UIColor whiteColor].CGColor;
    //_textView.layer.borderWidth = 1.0;
    _textView.layer.cornerRadius = 5.0;
    if(_textView.text.length == 0)
        _textView.text = NSLocalizedString(@"Enter here text for encryption/decryption...",nil);
}

-(void)textViewDidBeginEditing:(UITextView *)textView
{
    if([textView.text isEqualToString:NSLocalizedString(@"Enter here text for encryption/decryption...",nil)])
        textView.text = @"";
}
-(void)textViewDidEndEditing:(UITextView *)textView
{
    if(textView.text.length == 0)
        textView.text = NSLocalizedString(@"Enter here text for encryption/decryption...",nil);
}

@end
