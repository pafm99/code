//
//  PassCell.m
//  Text Encryption
//
//  Created by Grzegorz Wójcik on 06.05.2015.
//  Copyright (c) 2015 Grzegorz Wójcik. All rights reserved.
//

#import "PassCell.h"

@implementation PassCell

- (void)awakeFromNib {
    //_textField.layer.borderColor = [UIColor whiteColor].CGColor;
    //_textField.layer.borderWidth = 1.0;
    _textField.layer.cornerRadius = 5.0;
    _textField.placeholder = NSLocalizedString(@"Enter here password...",nil);
}

- (void)setSelected:(BOOL)selected animated:(BOOL)animated {
    [super setSelected:selected animated:animated];

    // Configure the view for the selected state
}
-(BOOL)textFieldShouldReturn:(UITextField *)textField
{
    [textField resignFirstResponder];
    return YES;
}

@end
