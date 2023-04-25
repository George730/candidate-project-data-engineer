drop table if exists `email_type`;
create table `email_type` (
    `type` varchar(128) not null,
    `email_type_id` int not null,
    `created` varchar(20) not null ,
    `created_by` varchar(128) not null,
    `updated` varchar(20),
    `updated_by` varchar(128)
	/* primary key (email_type_id) */
);

drop table if exists `phone_number_type`;
create table `phone_number_type` (
    `type` varchar(128) not null,
    `phone_number_type_id` int not null,
    `created` varchar(20) not null ,
    `created_by` varchar(128) not null,
    `updated` varchar(20),
    `updated_by` varchar(128)
	/* primary key (phone_number_type_id) */
);

drop table if exists `role_profile_type`;
create table `role_profile_type` (
    `type` varchar(128) not null,
    `role_profile_type_id` int not null,
    `created` varchar(20) not null ,
    `created_by` varchar(128) not null,
    `updated` varchar(20),
    `updated_by` varchar(128)
	/* primary key (role_profile_type_id) */
);

drop table if exists `user_profile`;
create table `user_profile` (
    `user_profile_id` varchar(128) not null,
    `first_name` varchar(128) not null,
    `last_name` varchar(128) not null,
    `created` varchar(20) not null ,
    `created_by` varchar(128) not null,
    `updated` varchar(20),
    `updated_by` varchar(128)
	/* primary key (user_profile_id) */
);

drop table if exists `user`;
create table `user` (
    `user_profile_id` varchar(128) not null,
	`user_id` int not null,
	`created` varchar(20) not null ,
    `created_by` varchar(128) not null,
    `updated` varchar(20),
    `updated_by` varchar(128)
	/* primary key (user_id), */
    /* foreign key (user_profile_id) references user_profile (user_profile_id) */
);

drop table if exists `role_profile`;
create table `role_profile` (
    `role_profile_id` int not null,
    `user_id` int,
    `role_profile_type_id` int,
    `created` varchar(20) not null ,
    `created_by` varchar(128) not null,
    `updated` varchar(20),
    `updated_by` varchar(128)
	/* primary key (role_profile_id), */
    /* foreign key (role_profile_type_id) references role_profile_type (role_profile_type_id), */
    /* foreign key (user_id) references user (user_id) */
);

drop table if exists `address`;
create table `address` (
    `address_id` int not null,
    `street` varchar(128),
	`city` varchar(128) not null,
	`state` varchar(64) not null,
    `zip_code` varchar(32) not null,
    `role_profile_id` int,
    `created` varchar(20) not null ,
    `created_by` varchar(128) not null,
    `updated` varchar(20),
    `updated_by` varchar(128)
	/* primary key (address_id), */
    /* foreign key (role_profile_id) references role_profile (role_profile_id) */
);

drop table if exists `email`;
create table `email` (
    `email_id` int not null,
    `value` varchar(20) not null,
    `email_type_id` int not null,
    `role_profile_id` int not null,
    `created` varchar(20) not null ,
    `created_by` varchar(128) not null,
    `updated` varchar(20),
    `updated_by` varchar(128)
	/* primary key (email_id), */
    /* foreign key (email_type_id) references email_type (email_type_id), */
    /* foreign key (role_profile_id) references role_profile (role_profile_id) */
);

drop table if exists `phone_number`;
create table `phone_number` (
    `phone_number_id` int not null,
    `phone_number_type_id` int,
    `role_profile_id` int,
    `value` varchar(20) not null,
    `created` varchar(20) not null ,
    `created_by` varchar(128) not null,
    `updated` varchar(20),
    `updated_by` varchar(128)
	/* primary key (phone_number_id), */
    /* foreign key (phone_number_type_id) references phone_number_type (phone_number_type_id), */
    /* foreign key (role_profile_id) references role_profile (role_profile_id) */
);
